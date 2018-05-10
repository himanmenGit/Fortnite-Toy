from django.conf import settings
from pfaw import Fortnite, Platform, Mode


def getFortnite():
    USERNAME = 'himanmen'

    fortnite = Fortnite(
        fortnite_token=settings.FORTNITE_AUTHORIZATION,
        launcher_token=settings.EPIC_LAUNCHER_AUTHORIZATION,
        email=settings.EPIC_EMAIL,
        password=settings.EPIC_PASSWORD,
    )

    player = fortnite.player(username=USERNAME)

    print(player.name)
    print(player.id)

    stats = fortnite.battle_royale_stats(username=USERNAME, platform=Platform.pc)
    solo = stats.solo
    duo = stats.duo
    squad = stats.squad
    all = stats.all

    return {
        'player': {
            'name': player.name,
            'id': player.id
        },
        'wins': {
            'solo': solo.wins,
            'duo': duo.wins,
            'squad': squad.wins,
            'all': all.wins,
        },
        'stats': {
            'solo': {
                'score': solo.score,
                'matches': solo.matches,
                'time': solo.time,
                'kills': solo.kills,
                'top3': solo.top3,
                'top5': solo.top5,
                'top6': solo.top6,
                'top10': solo.top10,
                'top12': solo.top12,
                'top25': solo.top25,
            },
            'duo': {
                'score': duo.score,
                'matches': duo.matches,
                'time': duo.time,
                'kills': duo.kills,
                'top3': duo.top3,
                'top5': duo.top5,
                'top6': duo.top6,
                'top10': duo.top10,
                'top12': duo.top12,
                'top25': duo.top25,
            },
            'squad': {
                'score': squad.score,
                'matches': squad.matches,
                'time': squad.time,
                'kills': squad.kills,
                'top3': squad.top3,
                'top5': squad.top5,
                'top6': squad.top6,
                'top10': squad.top10,
                'top12': squad.top12,
                'top25': squad.top25,
            },
            'all': {
                'score': all.score,
                'matches': all.matches,
                'time': all.time,
                'kills': all.kills,
                'top3': all.top3,
                'top5': all.top5,
                'top6': all.top6,
                'top10': all.top10,
                'top12': all.top12,
                'top25': all.top25,
            }
        }
    }
    # status = fortnite.server_status()
    #
    # if status:
    #     print('Servers are UP!')
    # else:
    #     print('Servers are DOWN.')
    #
    # news = fortnite.news()
    #
    # for br_news in news.br:
    #     print(br_news.image)
    #     print(br_news.title)
    #     print(br_news.body)
    #
    # store = fortnite.store()
    #
    # print(store.refresh_interval_hrs)
    # print(store.daily_purchase_hrs)
    # print(store.expiration)
    #
    # for front in store.storefronts:
    #     print(front.name)
    #
    #     for entry in front.catalog_entries:
    #         print(entry.offer_id)
    #         print(entry.dev_name)
    #         print(entry.offer_type)
    #         print(entry.title)
    #         print(entry.description)
    #         print(entry.refundable)
    #
    #         for price in entry.prices:
    #             print(price.currency_type)
    #             print(price.regular_price)
    #             print(price.final_price)
    #             print(price.sale_expiration)
    #             print(price.base_price)
    #
    # leaderboard = fortnite.leaderboard(count=10, platform=Platform.pc, mode=Mode.solo)
    #
    # for player in leaderboard:
    #     print(f'{player.id} - {player.name} - {player.rank} - {player.value}')


if __name__ == "__main__":
    getFortnite()
