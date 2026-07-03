# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pidi <pidi@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/02 20:40:47 by pidi              #+#    #+#              #
#    Updated: 2026/07/02 20:48:52 by pidi             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	d1 = int(input("Day 1 harvest: "))
	d2 = int(input("Day 2 harvest: "))
	d3 = int(input("Day 3 harvest: "))
	print(f"Total harvest: {d1 + d2 + d3}")
