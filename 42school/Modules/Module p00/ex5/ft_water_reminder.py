# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pidi <pidi@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/02 21:10:21 by pidi              #+#    #+#              #
#    Updated: 2026/07/02 22:11:13 by pidi             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))

    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
		