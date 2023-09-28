import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menú Pygame')

# Cargar la imagen de fondo
background_image = pygame.image.load('img/beast.jpg')  # Cambia la ruta por la de tu imagen
background_rect = background_image.get_rect()

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Fuente para el texto
font = pygame.font.Font(None, 36)

def draw_menu():
    # Dibujar el fondo
    screen.blit(background_image, background_rect)
    
    continue_button = font.render("Continuar", True, white)  # Nueva opción
    play_button = font.render("Nuevo Juego", True, white)
    quit_button = font.render("Salir", True, white)
    
    # Posiciones de los botones
    continue_rect = continue_button.get_rect(center=(screen_width/2, screen_height/2 - 100))  # Nueva posición
    play_rect = play_button.get_rect(center=(screen_width/2, screen_height/2 ))
    quit_rect = quit_button.get_rect(center=(screen_width/2, screen_height/2 + 100))
    
    screen.blit(continue_button, continue_rect)  # Dibujar la nueva opción
    screen.blit(play_button, play_rect)
    screen.blit(quit_button, quit_rect)
    
    return continue_rect,play_rect, quit_rect  # Ajustar el retorno de las posiciones

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):  # Nueva acción
                    print("Continuar juego")
                    # Aquí puedes poner la lógica para continuar el juego
                elif play_rect.collidepoint(event.pos):
                    print("Iniciar juego")
                    # Aquí puedes poner la lógica para iniciar el juego
                elif quit_rect.collidepoint(event.pos):
                    print("Salir del juego")
                    pygame.quit()
                    sys.exit()
        
        continue_rect, play_rect, quit_rect = draw_menu()  # Actualizar las posiciones
        
        pygame.display.flip()

if __name__ == '__main__':
    main()
