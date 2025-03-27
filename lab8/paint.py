import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    radius = 5  
    draw_mode = 'pen'
    start_pos = None
    current_color = (0, 0, 255)
    points = []
    shapes = []

    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0, 0, 0))

    running = True
    while running:
        screen.blit(canvas, (0, 0))

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    running = False
                if event.key == pygame.K_F4 and alt_held:
                    running = False
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_1:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    current_color = (0, 0, 255)

                if event.key == pygame.K_p:
                    draw_mode = 'pen'
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_r:
                    draw_mode = 'rect'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos  
                    if draw_mode == 'pen':
                        points.append((event.pos, current_color)) 
                    elif draw_mode == 'eraser':
                        pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius)
                elif event.button == 3:
                    radius = max(1, radius - 1)  

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    if draw_mode == 'rect':
                        shapes.append(("rect", start_pos, end_pos, current_color))
                    elif draw_mode == 'circle':
                        shapes.append(("circle", start_pos, end_pos, current_color))

            if event.type == pygame.MOUSEMOTION:
                if draw_mode == 'pen' and pygame.mouse.get_pressed()[0]:
                    points.append((event.pos, current_color)) 
                elif draw_mode == 'eraser' and pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius)

        canvas.fill((0, 0, 0))

        for i in range(len(points) - 1):
            drawLineBetween(canvas, points[i], points[i + 1], radius)

        for shape in shapes:
            shape_type, start, end, color = shape
            if shape_type == "rect":
                x1, y1 = start
                x2, y2 = end
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color, rect, 5)
            elif shape_type == "circle":
                dx = end[0] - start[0]
                dy = end[1] - start[1]
                temp_radius = int((dx ** 2 + dy ** 2) ** 0.5)
                pygame.draw.circle(canvas, color, start, temp_radius, 5)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, point1, point2, width):
    start, color1 = point1
    end, color2 = point2

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        
        color = (
            int(aprogress * color1[0] + progress * color2[0]),
            int(aprogress * color1[1] + progress * color2[1]),
            int(aprogress * color1[2] + progress * color2[2])
        )
        
        pygame.draw.circle(surface, color, (x, y), width)

main()
