{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0efdd935",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random \n",
    "\n",
    "color = input(\"What color is rose?: \")\n",
    "print(color)\n",
    "\n",
    "player_score = 0\n",
    "computer_score = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ec494bb8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-13-516a60aea710>, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-13-516a60aea710>\"\u001b[1;36m, line \u001b[1;32m11\u001b[0m\n\u001b[1;33m    if player ==\u001b[0m\n\u001b[1;37m                 ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Rock, Paper, Scissors!\")\n",
    "game_total = input(\"Would you like to play best of 1, best of 3 or best of 5? Please respond with 1, 3 or 5\")\n",
    "print(game_total)\n",
    "\n",
    "player = input(\"Rock, Paper or Scissors?\")\n",
    "print(player)\n",
    "\n",
    "def game():\n",
    "    \n",
    "    player_choice()\n",
    "    computer_choice()\n",
    "    \n",
    "def result(player, computer):\n",
    "    if player == computer:\n",
    "        return \"Draw!\" \n",
    "    elif player == \"rock\" and computer == \"paper\":\n",
    "        computer_score += 1\n",
    "        print()\n",
    "        return \"Point for Computer!\"  \n",
    "    \n",
    "if player_score or computer_score == game_total:\n",
    "    if player_score > computer_score:\n",
    "        print(\"Player wins!\")\n",
    "    else:\n",
    "        print(\"Computer wins!\")\n",
    "    answer = input(\"Would you like to play again? Y/N\")\n",
    "    play_again(answer)\n",
    "    \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c4f91535",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "print(random.randint(1,3))\n",
    "print(random.randint(1,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f0d7a0c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def computer_choice()\n",
    "    computer = random.randint(1,3)\n",
    "    if computer == 1:\n",
    "        return \"rock\"\n",
    "    elif computer == 2:\n",
    "        return \"paper\"\n",
    "    elif computer == 3:\n",
    "        return \"scissors\"\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2ed4ebad",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-12-91a34f616896>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-12-91a34f616896>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    def play()\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def play_again(res):\n",
    "    if answer == \"Y\":\n",
    "        def play()\n",
    "    else:\n",
    "        return \"Thank you for playing!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b31ff3b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
