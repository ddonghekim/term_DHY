import gym
import time # sleep(초) 사용을 위해

env = gym.make("SpaceInvaders-v0")
num_actions = env.action_space.n

for episode in range(1):
    observation = env.reset()

    for step in range(100000):
        env.render()
        time.sleep(0.01) # 화면 표시 딜레이를 위해

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if(done):
            print('episode ',episode,' finished after ',step+1,'steps')
            break

env.close()