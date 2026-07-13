# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pidi <pidi@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/02 22:20:40 by pidi              #+#    #+#              #
#    Updated: 2026/07/09 16:22:44 by pidi             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed: str, q: int, unit: str) -> None:
	seed = seed.capitalize()

	match unit:
		case "area":
			print(f"{seed} seeds: covers {q} square meters")
		case "grams":
			print(f"{seed} seeds: {q} grams total")
		case "packets":
			print(f"{seed} seeds: {q} packets available")
		case _:
			print("Unknown unit type")
