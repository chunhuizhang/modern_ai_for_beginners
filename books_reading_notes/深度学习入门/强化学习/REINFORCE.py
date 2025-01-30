# %% - Andriy Drozdyuk

import torch
import gym
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

max_steps = 50_000
step = 0
lr = 0.005
γ = 0.9999
# Add parameters for logging
episode_rewards = []
moving_avg_size = 100
reward_window = deque(maxlen=moving_avg_size)

env = gym.make('CartPole-v0')

nn = torch.nn.Sequential(
    torch.nn.Linear(4, 64),
    torch.nn.ReLU(),
    torch.nn.Linear(64, env.action_space.n),
    torch.nn.Softmax(dim=-1)
)
optim = torch.optim.Adam(nn.parameters(), lr=lr)

while step <= max_steps:
    obs = torch.tensor(env.reset(), dtype=torch.float)    
    done = False
    Actions, States, Rewards = [], [], []

    while not done:
        probs = nn(obs)
        dist = torch.distributions.Categorical(probs=probs)        
        action = dist.sample().item()
        obs_, rew, done, _ = env.step(action)
        
        Actions.append(torch.tensor(action, dtype=torch.int))
        States.append(obs)
        Rewards.append(rew)

        obs = torch.tensor(obs_, dtype=torch.float)

        step += 1
        
    # Log episode total reward
    episode_reward = sum(Rewards)
    episode_rewards.append(episode_reward)
    reward_window.append(episode_reward)
    moving_avg = np.mean(list(reward_window))
    
    if len(episode_rewards) % 10 == 0:
        print(f'Episode {len(episode_rewards)}, Steps: {step}, '
              f'Last Reward: {episode_reward:.1f}, '
              f'Moving Average: {moving_avg:.1f}')
    
    DiscountedReturns = []
    # G0, G1, G2, ...
    for t in range(len(Rewards)):
        G = 0.0
        for k, r in enumerate(Rewards[t:]):
            G += (γ**k)*r
        DiscountedReturns.append(G)
    
    for State, Action, G in zip(States, Actions, DiscountedReturns):
        probs = nn(State)
        dist = torch.distributions.Categorical(probs=probs)    
        log_prob = dist.log_prob(Action)
        
        loss = - log_prob*G
        
        optim.zero_grad()
        loss.backward()
        optim.step()

# Add visualization before playing
plt.figure(figsize=(10, 5))
plt.plot(episode_rewards, alpha=0.3, label='Episode Rewards')
plt.plot(np.convolve(episode_rewards, 
                     np.ones(moving_avg_size)/moving_avg_size, 
                     mode='valid'),
         label=f'Moving Average ({moving_avg_size})')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress')
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('./figs/REINFORCE.png')


# %% Play

for _ in range(5):
    Rewards = []
    
    obs = torch.tensor(env.reset(), dtype=torch.float)    
    done = False
    env.render()
    
    while not done:
        probs = nn(obs)
        c = torch.distributions.Categorical(probs=probs)        
        action = c.sample().item()
        
        obs_, rew, done, _info = env.step(action)
        env.render()

        obs = torch.tensor(obs_, dtype=torch.float)

        Rewards.append(rew)
    

    print(f'Reward: {sum(Rewards)}')
env.close()
# %%