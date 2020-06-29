def update_screen(ai_settings,screen,rocket):
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()
