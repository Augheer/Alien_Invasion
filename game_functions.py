import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	'''Respond to keypresses and mouse events.'''
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)
				

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	'''Respond to keypresses.'''
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right.
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# Create a new bullet and add it to the bullets group.
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	'''Fire a bullet if limit not reached yet.'''
	# Create a new bullet and add it to the bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	'''Respond to key releases'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
	'''Update images on the screen and flip to the new screen.'''
	screen.fill(ai_settings.bg_colour)
	ship.blitme()
	# Redraw ll bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()


	# Make the game display the most recently drawn screen.
	pygame.display.flip()


def update_bullets(bullets):
	'''Update the position of the bullets and get rid of old bullets.'''
	# Update bullet positions.
	bullets.update()

	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		print(len(bullets))