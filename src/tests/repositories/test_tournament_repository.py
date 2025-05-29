import pytest

from src.domain.entities.tournaments import Tournament


def make_tournament(tournament_id: int, user_id: int) -> Tournament:
    return Tournament.from_bets(
        tournament_id=tournament_id,
        title=f"Tournament #{tournament_id}",
        bank=1000,
        user_id=user_id,
        bets=[],
    )


@pytest.mark.asyncio
async def test_tournament_repo_add_and_get(tournament_repo):
    tournament = make_tournament(1, 42)

    await tournament_repo.add(tournament)
    fetched = await tournament_repo.get_by_id(1)

    assert fetched == tournament, f"{fetched=}"


@pytest.mark.asyncio
async def test_tournament_repo_update(tournament_repo):
    tournament = make_tournament(2, 42)
    await tournament_repo.add(tournament)

    updated = Tournament.from_bets(
        tournament_id=2,
        title="Updated Title",
        bank=2000,
        user_id=42,
        bets=[],
    )
    result = await tournament_repo.update(updated)

    assert result.title == "Updated Title", f"{result.title=}"
    fetched = await tournament_repo.get_by_id(2)
    assert fetched.bank == 2000, f"{fetched.bank=}"


@pytest.mark.asyncio
async def test_tournament_repo_delete(tournament_repo):
    tournament = make_tournament(3, 42)
    await tournament_repo.add(tournament)

    deleted = await tournament_repo.delete(3)
    assert deleted is True, f"{deleted=}"

    fetched = await tournament_repo.get_by_id(3)
    assert fetched is None, f"{fetched=}"


@pytest.mark.asyncio
async def test_tournament_repo_delete_nonexistent(tournament_repo):
    deleted = await tournament_repo.delete(tournament_id=99)
    assert deleted is False, f"{deleted=}"
