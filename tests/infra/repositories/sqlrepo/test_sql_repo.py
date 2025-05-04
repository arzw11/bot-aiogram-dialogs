import pytest

from src.bets.entity import (
    Bet as BetEntity,
    BetResult,
)
from src.tournaments.entity import Tournament as TournamentEntity


@pytest.mark.asyncio
async def test_sql_user_repo_add(user_repo, user_entity):
    await user_repo.add(user=user_entity)
    count_users = await user_repo.count_users()

    assert count_users == 1, f"{count_users=}"


@pytest.mark.asyncio
async def test_sql_user_repo_add_and_get_by_id_exist(user_repo, user_entity):
    retrieved_user = await user_repo.get_by_id(1)

    assert retrieved_user is not None, f"{retrieved_user=}"
    assert retrieved_user.user_id == user_entity.user_id, f"{retrieved_user.user_id=}"
    assert retrieved_user.telegram_id == user_entity.telegram_id, f"{retrieved_user.telegram_id=}"
    assert retrieved_user.name == user_entity.name, f"{retrieved_user.name=}"


@pytest.mark.asyncio
async def test_sql_user_repo_add_and_get_by_telegram_id_exist(user_repo, user_entity):
    retrieved_user = await user_repo.get_by_telegram_id(123121)

    assert retrieved_user is not None, f"{retrieved_user=}"
    assert retrieved_user.user_id == user_entity.user_id, f"{retrieved_user.user_id=}"
    assert retrieved_user.telegram_id == user_entity.telegram_id, f"{retrieved_user.telegram_id=}"
    assert retrieved_user.name == user_entity.name, f"{retrieved_user.name=}"


@pytest.mark.asyncio
async def test_sql_user_repo_add_and_get_by_id_not_exist(user_repo):
    retrieved_user = await user_repo.get_by_id(99999)

    assert retrieved_user is None, f"{retrieved_user=}"


@pytest.mark.asyncio
async def test_sql_user_repo_add_and_get_by_telegram_id_not_exist(user_repo):
    retrieved_user = await user_repo.get_by_telegram_id(999999)

    assert retrieved_user is None, f"{retrieved_user=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_add(bet_repo, list_bet_entities):
    for bet in list_bet_entities:
        await bet_repo.add(bet=bet)

    count_bets = await bet_repo.count_bets()

    assert count_bets == 3, f"{count_bets=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_bet_by_id_exist(bet_repo, list_bet_entities):
    first_bet = list_bet_entities[0]
    second_bet = list_bet_entities[1]

    bet1 = await bet_repo.get_by_id(bet_id=first_bet.bet_id)
    bet2 = await bet_repo.get_by_id(bet_id=second_bet.bet_id)

    assert bet1 is not None, f"{bet1=}"
    assert bet1 == first_bet, f"{bet1=}"
    assert bet2 is not None, f"{bet2=}"
    assert bet2 == second_bet, f"{bet2=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_bet_by_user_id_not_exist(bet_repo):
    bet = await bet_repo.get_by_id(bet_id=9999)

    assert bet is None, f"{bet=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_all_by_user_id_exist(bet_repo, list_bet_entities):
    bets = await bet_repo.get_all_by_user_id(list_bet_entities[0].user_id)

    assert bets is not None, f"{bets=}"
    assert len(bets) == len(list_bet_entities), f"{len(bets)}"
    assert bets == list_bet_entities, f"{bets=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_all_by_user_id_not_exist(bet_repo):
    bets = await bet_repo.get_all_by_user_id(9999)

    assert bets is None, f"{bets=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_all_by_tournament_id_exist(bet_repo, list_bet_entities):
    tournament_id = list_bet_entities[0].tournament_id
    len_bets_of_list_bet_entities = 0

    for bet in list_bet_entities:
        if bet.tournament_id == tournament_id:
            len_bets_of_list_bet_entities += 1

    bets = await bet_repo.get_all_by_tournament_id(tournament_id)

    assert bets is not None, f"{bets=}"
    assert len(bets) == len_bets_of_list_bet_entities, f"{len(bets)=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_get_all_by_tournament_id_not_exist(bet_repo):
    bets = await bet_repo.get_all_by_tournament_id(3333)

    assert bets is None, f"{bets=}"


@pytest.mark.asyncio
async def test_sql_bet_repo_update_exist(bet_repo, list_bet_entities):
    bet = BetEntity.from_result(
        bet_id=3,
        user_id=1,
        tournament_id=2,
        amount=20000,
        odds=2,
        result=BetResult.WIN,
    )
    result = await bet_repo.update(bet)

    third_bet = list_bet_entities[-1]
    updated_bet = await bet_repo.get_by_id(bet.bet_id)

    assert result, f"{result}"
    assert updated_bet == bet, f"{updated_bet}"
    assert updated_bet.amount != third_bet.amount, f"{updated_bet.amount}"
    assert updated_bet.payout != third_bet.payout, f"{updated_bet.payout}"


@pytest.mark.asyncio
async def test_sql_bet_repo_update_not_exist(bet_repo, list_bet_entities):
    bet = BetEntity.from_result(
        bet_id=22222,
        user_id=1,
        tournament_id=2,
        amount=20000,
        odds=2,
        result=BetResult.WIN,
    )
    result = await bet_repo.update(bet)

    assert not result, f"{result}"


@pytest.mark.asyncio
async def test_sql_bet_repo_delete_exist(bet_repo, list_bet_entities):
    bet_id = list_bet_entities[-1].bet_id
    result = await bet_repo.delete(bet_id)

    count_bets = await bet_repo.count_bets()

    assert result, f"{result=}"
    assert count_bets != len(list_bet_entities), f"{count_bets=}"


@pytest.mark.asyncio
async def test_sql_user_repo_get_bets_exist(user_repo, user_entity):
    user_id = user_entity.user_id
    bets = await user_repo.get_bets(user_id)

    assert bets is not None, f"{bets=}"
    assert isinstance(bets, list), f"{type(bets)=}"
    assert len(bets) == 2, f"{len(bets)=}"


@pytest.mark.asyncio
async def test_sql_user_repo_get_bets_not_exist(user_repo):
    bets = await user_repo.get_bets(131)

    assert not bets, f"{bets=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_add(tournament_repo, list_tournament_entities):
    for tournament in list_tournament_entities:
        await tournament_repo.add(tournament)

    count_tournaments = await tournament_repo.count_tournaments()

    assert count_tournaments == len(list_tournament_entities), f"{count_tournaments}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_get_by_id_exist(tournament_repo, list_tournament_entities):
    first_tournament = list_tournament_entities[0]
    second_tournament = list_tournament_entities[1]

    tournament1 = await tournament_repo.get_by_id(first_tournament.tournament_id)
    tournament2 = await tournament_repo.get_by_id(second_tournament.tournament_id)

    assert tournament1 is not None, f"{tournament1=}"
    assert tournament1 == first_tournament, f"{tournament1=}"
    assert tournament2 is not None, f"{tournament2=}"
    assert tournament2 == second_tournament, f"{tournament2=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_get_by_id_not_exist(tournament_repo):
    tournament = await tournament_repo.get_by_id(tournament_id=9999)

    assert tournament is None, f"{tournament=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_update_exist(tournament_repo, list_tournament_entities):
    tournament = TournamentEntity.from_bets(
        tournament_id=2,
        title="EXAMPLE2",
        bank=10000,
        user_id=1,
        bets=None,
    )
    result = await tournament_repo.update(tournament)
    second_tournament = list_tournament_entities[-1]

    updated_tournament = await tournament_repo.get_by_id(tournament.tournament_id)

    assert result, f"{result=}"
    assert updated_tournament == tournament, f"{updated_tournament=}"
    assert updated_tournament.bank != second_tournament.bank, f"{updated_tournament.bank=}"
    assert updated_tournament.title != second_tournament.title, f"{updated_tournament.title=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_update_not_exist(tournament_repo):
    tournament = TournamentEntity.from_bets(
        tournament_id=1231,
        title="EXAMPLE2",
        bank=10000,
        user_id=1,
        bets=None,
    )
    result = await tournament_repo.update(tournament)

    assert result, f"{result=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_delete_exist(tournament_repo, list_tournament_entities):
    tournament_id = list_tournament_entities[-1].tournament_id
    result = await tournament_repo.delete(tournament_id)

    count_tournaments = await tournament_repo.count_tournaments()

    assert result, f"{result=}"
    assert count_tournaments != len(list_tournament_entities), f"{count_tournaments=}"


@pytest.mark.asyncio
async def test_sql_tournament_repo_delete_not_exist(tournament_repo):
    result = await tournament_repo.delete(32131)

    assert not result, f"{result=}"


@pytest.mark.asyncio
async def test_sql_user_repo_get_tournaments_exist(user_repo, user_entity):
    tournaments = await user_repo.get_tournaments(user_entity.user_id)

    assert tournaments is not None, f"{tournaments=}"


@pytest.mark.asyncio
async def test_sql_user_repo_get_tournaments_not_exist(user_repo, user_entity):
    tournaments = await user_repo.get_tournaments(222)

    assert tournaments is None, f"{tournaments=}"
