print('Importando as bibliotecas do processo...')
import gym
from neoricalex.envs.ambiente import Ambiente

if __name__ == '__main__':
    print('Iniciando as checkagens Pré-Mundo...')
    env = gym.make('neoricalex-v0')
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
    env.close()

