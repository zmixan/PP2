import pygame

songs = ["OM NOM NOM.mp3", "New Jeans - Jersey Club - Slowed Down.mp3", "Automotivo Bibi Forgosa.mp3", "The Automotivo Infernal.mp3"]
cur_ind = 0
is_playing = True

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("AudioPlayer")

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False

            elif event.key == pygame.K_RIGHT:
                cur_ind = (cur_ind + 1) % len(songs)
                pygame.mixer.music.load(songs[cur_ind])
                pygame.mixer.music.play()
                is_playing = True

            elif event.key == pygame.K_LEFT:
                cur_ind = (cur_ind - 1) % len(songs)
                pygame.mixer.music.load(songs[cur_ind])
                pygame.mixer.music.play()
                is_playing = True

pygame.quit()