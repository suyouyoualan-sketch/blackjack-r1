import random

def draw_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def useable_ace(cards):
    if not(11 in cards):
        return 0
    else:
        return cards.count(11)

def handvalue(cards):
    value=0
    for card in cards:
        value += card
    if value <= 21:
        return value
    else:
        if not(11 in cards):
            return value
        else:
            ace_number=cards.count(11)
            for i in range(ace_number):
                value_i = value-10*(i+1)
                if value_i <= 21:
                    return value_i
                    break
            return value

class BlackjackEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.player = [draw_card(), draw_card()]
        self.dealer = [draw_card(), draw_card()]
        self.state = self.get_state()

    def get_state(self):
        return (handvalue(self.player),self.dealer[0],useable_ace(self.player)) # a tuple, first element is the handvalue of the player, second is the face-up card, third is the number of ace

    def step(self, action):
        terminated = False
        if action == 1: # Hit
            self.player.append(draw_card())
            self.state = self.get_state()
            if handvalue(self.player) > 21:
                reward = -1
                terminated = True
                return (self.state, reward, terminated) # Note that for this case, since the player already loses, dealer will not hit cards anymore.
            else:
                reward = 0
                terminated = False
                return (self.state, reward, terminated)
        elif action == 0: # Stand
            while handvalue(self.dealer) < 17:
                self.dealer.append(draw_card())
                self.state = self.get_state()
            if handvalue(self.dealer) > 21 or handvalue(self.player) > handvalue(self.dealer):
                reward = 1
                terminated = True
                return (self.state, reward, terminated)
            elif handvalue(self.dealer) == handvalue(self.player):
                reward = 0
                terminated = True
                return (self.state, reward, terminated)
            else:
                reward = -1
                terminated = True
                return (self.state, reward, terminated)

# # Test 1
# env = BlackjackEnv()
# print("Player: ",env.player)
# print("Dealer: ",env.dealer)
#
# # Test 2.1: hit
# state, reward, terminated = env.step(1)
# print("Player hit: ",env.player)
# print("Dealer result: ",env.dealer)
# print("Final state:", state, "reward:", reward, "terminated:", terminated)

# # Test 2.2: stand
# state, reward, terminated = env.step(0)
# print("Player stand: ",env.player)
# print("Dealer result: ",env.dealer)
# print("Final state:", state, "reward:", reward, "terminated:", terminated)


# env = BlackjackEnv()
# print("Player: ",env.player)
# print("Dealer: ",env.dealer)
# print("State: ",env.state)