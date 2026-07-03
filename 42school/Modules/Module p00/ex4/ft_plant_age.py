# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pidi <pidi@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/02 20:49:25 by pidi              #+#    #+#              #
#    Updated: 2026/07/02 21:01:27 by pidi             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	days = int(input("Enter plant age in days: "))
	if (days <= 60):
		print("Plant needs more time to grow.")
	else:
		print("Plant is ready to harvest!")
