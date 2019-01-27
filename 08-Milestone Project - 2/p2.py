import account
import random


def init_deck():
    npc_deck = []
    human_deck = []
    common_deck = ['A' + str(i + 1) for i in range(13)]
    common_deck += ['B' + str(i + 1) for i in range(13)]
    common_deck += ['C' + str(i + 1) for i in range(13)]
    common_deck += ['D' + str(i + 1) for i in range(13)]
    return npc_deck, human_deck, common_deck


def get_point(deck):
    point = sum(map(lambda x: int(x[1:]), deck))
    if point > 21:
        point = 0
    return point


def main():
    npc = account.Account()
    human = account.Account()

    npc_deck, human_deck, common_deck = init_deck()

    while npc.mymoney > 0 and human.mymoney > 0:
        if len(human_deck) < 5:
            ask_more = input('do you want more?(Y/N)').lower() == 'y'
        else:
            ask_more = False

        if ask_more:
            one_card = random.choice(common_deck)
            human_deck.append(one_card)
            print(human_deck)
            one_card = random.choice(common_deck)
            npc_deck.append(one_card)
        else:
            human_point = get_point(human_deck)
            npc_point = get_point(npc_deck)
            if human_point > npc_point:
                human.add_money(human_point - npc_point)
                npc.remove_money(human_point - npc_point)
            else:
                npc.add_money(-human_point + npc_point)
                human.remove_money(-human_point + npc_point)
            print('Human deck = {0}, total point = {1}, money = {2}'.format(human_deck, human_point, human.mymoney))
            print('NPC deck = {0}, total point = {1}, money = {2}'.format(npc_deck, npc_point, npc.mymoney))
            npc_deck, human_deck, common_deck = init_deck()
    print('human money = {0}, npc money = {1}'.format(human.mymoney, npc.mymoney))


if __name__ == '__main__':
    main()
