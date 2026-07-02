# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pidi <pidi@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/02 22:12:18 by pidi              #+#    #+#              #
#    Updated: 2026/07/02 22:19:29 by pidi             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	def count_day(day):
		if day > days:
			print("Harvest time!")
			return
		print(f"Day {day}")
		count_day(day + 1)
	count_day(1)

''' def ft_count_harvest_recursive(day=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1, days)'''