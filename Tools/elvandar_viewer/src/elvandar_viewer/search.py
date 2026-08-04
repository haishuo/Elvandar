from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .repository import SUPPORTED_SUFFIXES
from .repository_view import RepositoryView


_MARKDOWN_DECORATION = re.compile(r"(?:[*_`#>|\[\]]|!\[[^]]*\]\([^)]*\))")
_WHITESPACE = re.compile(r"\s+")


@dataclass(frozen=True, slots=True)
class SearchDocument:
    path: Path
    title: str
    location: str
    source: str
    plain: str
    searchable: str


@dataclass(frozen=True, slots=True)
class SearchResult:
    path: Path
    title: str
    location: str
    excerpt: str
    score: int
    matches: int


class SearchIndex:
    def __init__(self) -> None:
        self._documents: dict[Path, SearchDocument] = {}

    def rebuild(self, repository: RepositoryView) -> None:
        documents = repository.read_documents()
        rebuilt = {
            repository.resolve(path): self._document(repository, path, source)
            for path, source in documents.items()
        }
        self._documents = rebuilt

    def update(self, repository: RepositoryView, path: Path) -> None:
        path = repository.resolve(path)
        if path.suffix.casefold() not in SUPPORTED_SUFFIXES or not repository.is_file(path):
            self._documents.pop(path, None)
            return
        try:
            source = repository.read_text(path)
        except (OSError, ValueError):
            return
        self._add(repository, path, source)

    def search(self, query: str, limit: int = 100) -> list[SearchResult]:
        phrase = _WHITESPACE.sub(" ", query.casefold()).strip()
        terms = list(dict.fromkeys(phrase.split()))
        if not terms:
            return []

        results: list[SearchResult] = []
        for document in self._documents.values():
            if not all(term in document.searchable for term in terms):
                continue
            title = document.title.casefold()
            location = document.location.casefold()
            source = document.source.casefold()
            title_hits = sum(title.count(term) for term in terms)
            path_hits = sum(location.count(term) for term in terms)
            body_hits = sum(source.count(term) for term in terms)
            score = title_hits * 70 + path_hits * 24 + min(body_hits, 30) * 4
            if phrase == title:
                score += 500
            elif title.startswith(phrase):
                score += 220
            elif phrase in title:
                score += 130
            if phrase in source:
                score += 35
            results.append(
                SearchResult(
                    path=document.path,
                    title=document.title,
                    location=document.location,
                    excerpt=_excerpt(document.plain, phrase, terms),
                    score=score,
                    matches=body_hits + title_hits + path_hits,
                )
            )

        return sorted(results, key=lambda result: (-result.score, result.location.casefold()))[:limit]

    def _add(self, repository: RepositoryView, path: Path, source: str) -> None:
        document = self._document(repository, path, source)
        self._documents[document.path] = document

    @staticmethod
    def _document(repository: RepositoryView, path: Path, source: str) -> SearchDocument:
        path = repository.resolve(path)
        location = repository.relative(path).as_posix()
        title = path.stem
        searchable = f"{title}\n{location}\n{source}".casefold()
        plain = _WHITESPACE.sub(" ", _MARKDOWN_DECORATION.sub("", source)).strip()
        return SearchDocument(path, title, location, source, plain, searchable)


def _excerpt(plain: str, phrase: str, terms: list[str], length: int = 180) -> str:
    lowered = plain.casefold()
    position = lowered.find(phrase)
    if position < 0:
        positions = [lowered.find(term) for term in terms if lowered.find(term) >= 0]
        position = min(positions, default=0)
    start = max(0, position - length // 3)
    end = min(len(plain), start + length)
    start = _word_boundary(plain, start, forward=True) if start else 0
    end = _word_boundary(plain, end, forward=False) if end < len(plain) else len(plain)
    excerpt = plain[start:end].strip()
    return ("…" if start else "") + excerpt + ("…" if end < len(plain) else "")


def _word_boundary(text: str, position: int, *, forward: bool) -> int:
    if forward:
        boundary = text.find(" ", position)
        return boundary + 1 if boundary >= 0 else position
    boundary = text.rfind(" ", 0, position)
    return boundary if boundary >= 0 else position
