import pytest


@pytest.mark.asyncio
async def test_tournament_repo_add_and_get_tournament(tournament_repo, dummy_tournament):
    await tournament_repo.add(dummy_tournament)
    fetched = await tournament_repo.get_tournament(dummy_tournament.tournament_id)
    assert fetched == dummy_tournament, f"{fetched=}"
    assert fetched.bank == 1000, f"{fetched.bank=}"
    assert fetched.final_balance == 1100, f"{fetched.final_balance=}"


@pytest.mark.asyncio
async def test_tournament_repo_get_list_tournaments_by_user(tournament_repo, dummy_tournament, dummy_user):
    await tournament_repo.add(dummy_tournament)
    tournaments = await tournament_repo.get_list_tournaments_by_user(dummy_user.user_id)
    assert len(tournaments) == 1, f"{len(tournaments)=}"
    assert tournaments[0].tournament_id == dummy_tournament.tournament_id, f"{tournaments[0].tournament_id=}"


@pytest.mark.asyncio
async def test_tournament_repo_update_tournament(tournament_repo, dummy_tournament):
    await tournament_repo.add(dummy_tournament)
    updated = await tournament_repo.update_tournament(
        dummy_tournament.tournament_id, {
            "title": "Updated Tournament",
            "bank": 1200,
            "bets": dummy_tournament.bets,
        },
    )
    assert updated.title == "Updated Tournament", f"{updated.title=}"
    assert updated.bank == 1200, f"{updated.bank=}"
    assert updated.final_balance == 1300, f"{updated.final_balance=}"


@pytest.mark.asyncio
async def test_tournament_repo_delete_tournament(tournament_repo, dummy_tournament):
    await tournament_repo.add(dummy_tournament)
    deleted = await tournament_repo.delete_tournament(dummy_tournament.tournament_id)
    assert deleted == dummy_tournament, f"{deleted=}"
    with pytest.raises(KeyError):
        await tournament_repo.get_tournament(dummy_tournament.tournament_id)
