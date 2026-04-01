import pygame_menu
import pygame
import os
import json
import time
import random

pygame.init()

class Data_Setting():
    def __init__(self):
        self.screen_size = (1920, 1080)
        self.db = FileData()
        self.config_path = os.path.join(os.path.dirname(__file__), 'Setting_change.json')
        self.volume = 50
        self.load_settings()
        self.coins = User_Coins(self)
        self.selected_skin = 'default'

    def load_settings(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                data = json.load(f)
                self.volume = data.get('volume', 50)
                self.coins_amount = data.get('coins', 0)
                self.selected_skin = data.get('selected_skin', 'default')

        pygame.mixer.music.set_volume(self.volume / 100)

    def save_settings(self):
        data = {
            'volume': self.volume,
            'coins': self.coins.amount,
            'selected_skin': self.selected_skin
        }
        with open(self.config_path, 'w') as f:
            json.dump(data, f, indent=4)

class FileData():

    def __init__(self):
        self.script_path = os.path.dirname(__file__)
        self.sound_dir_path = os.path.join(self.script_path, 'Soundtracks')
        self.image_dir_path = os.path.join(self.script_path, 'Images')
        self.snakes_dir = os.path.join(self.image_dir_path, 'Snakes')
        self.static_evil_dir = os.path.join(self.image_dir_path, 'Static_Evil')
        self.dynamic_evil_dir = os.path.join(self.image_dir_path, 'Dimanic_Evil')
        self.object_dir = os.path.join(self.image_dir_path, 'Object')
        self.bg_dir = os.path.join(self.image_dir_path, 'Background')

        self.sound = {
            'mm_sound': os.path.join(self.sound_dir_path, 'sound2.mp3'),
            'apple_nom_sound': os.path.join(self.sound_dir_path, 'apple_get.mp3'),
            'coin_sound': os.path.join(self.sound_dir_path, 'coin_get.mp3'),
            'snake_heat_self': os.path.join(self.sound_dir_path, 'snake_self.mp3'),
            'snake_heat_border': os.path.join(self.sound_dir_path, 'snake_border.mp3'),
            'lvl1_sound': os.path.join(self.sound_dir_path, 'lvl1_sound.mp3'),
            'shop_menu_sound': os.path.join(self.sound_dir_path, 'shop_sound.mp3'),
            'hadgehog_sound': os.path.join(self.sound_dir_path, 'hadgehog_sound.mp3'),
            'eagle_sound': os.path.join(self.sound_dir_path, 'eagle_sound.mp3')
        }

        self.images = {
            'mm_menu_img': os.path.join(self.bg_dir, 'menu_img.png'),
            'st_menu_img': os.path.join(self.bg_dir, 'setng_menu.png'),
            'sh_menu_img': os.path.join(self.bg_dir, 'shop_menu.png'),
            'lvl1_bg': os.path.join(self.bg_dir, 'bg_1lvl_img.png'),
            'lvl2_bg': os.path.join(self.bg_dir, 'bg_2lvl_img.png'),
            'lvl3_bg': os.path.join(self.bg_dir, 'bg_3lvl_img.png'),
            'lvl4_bg': os.path.join(self.bg_dir, 'bg_4lvl_img.png'),
            'lvl5_bg': os.path.join(self.bg_dir, 'bg_5lvl_img.png'),
            'heart_elexir_icon': os.path.join(self.bg_dir, 'heart_elexir.png'),
            'Shooting_star_icon': os.path.join(self.bg_dir, 'shooting_star.png'),
            'inventory': os.path.join(self.bg_dir, 'inventory_menu.png'),

            'head_up': os.path.join(self.snakes_dir, 'head_up_img.png'),
            'head_down': os.path.join(self.snakes_dir, 'head_down_img.png'),
            'head_right': os.path.join(self.snakes_dir, 'head_right_img.png'),
            'head_left': os.path.join(self.snakes_dir, 'head_left_img.png'),
            'body_up': os.path.join(self.snakes_dir, 'body_up_img.png'),
            'body_left': os.path.join(self.snakes_dir, 'body_left_img.png'),
            'body_move': os.path.join(self.snakes_dir, 'body_move_img.png'),

            'red_up': os.path.join(self.snakes_dir, 'red_snake_head_up.png'),
            'red_down': os.path.join(self.snakes_dir, 'red_snake_head_down.png'),
            'red_right': os.path.join(self.snakes_dir, 'red_snake_head_right.png'),
            'red_left': os.path.join(self.snakes_dir, 'red_snake_head_left.png'),
            'red_goriz': os.path.join(self.snakes_dir, 'red_snake_gorizontal.png'),
            'red_vertical': os.path.join(self.snakes_dir, 'red_snake_vertical.png'),

            'blue_up': os.path.join(self.snakes_dir, 'blue_snake_head_up.png'),
            'blue_down': os.path.join(self.snakes_dir, 'blue_snake_head_down.png'),
            'blue_right': os.path.join(self.snakes_dir, 'blue_snake_head_right.png'),
            'blue_left': os.path.join(self.snakes_dir, 'blue_snake_head_left.png'),
            'blue_goriz': os.path.join(self.snakes_dir, 'blue_snake_gorizontal.png'),
            'blue_vertical': os.path.join(self.snakes_dir, 'blue_snake_vertical.png'),

            'yellow_up': os.path.join(self.snakes_dir, 'yellow_snake_head_up.png'),
            'yellow_down': os.path.join(self.snakes_dir, 'yellow_snake_head_down.png'),
            'yellow_right': os.path.join(self.snakes_dir, 'yellow_snake_head_right.png'),
            'yellow_left': os.path.join(self.snakes_dir, 'yellow_snake_head_left.png'),
            'yellow_goriz': os.path.join(self.snakes_dir, 'yellow_snake_gorizontal.png'),
            'yellow_vertical': os.path.join(self.snakes_dir, 'yellow_snake_vertical.png'),

            'purple_up': os.path.join(self.snakes_dir, 'purple_snake_head_up.png'),
            'purple_down': os.path.join(self.snakes_dir, 'purple_snake_head_down.png'),
            'purple_right': os.path.join(self.snakes_dir, 'purple_snake_head_right.png'),
            'purple_left': os.path.join(self.snakes_dir, 'purple_snake_head_left.png'),
            'purple_goriz': os.path.join(self.snakes_dir, 'purple_snake_gorizontal.png'),
            'purple_vertical': os.path.join(self.snakes_dir, 'purple_snake_vertical.png'),

            'orange_up': os.path.join(self.snakes_dir, 'orange_snake_head_up.png'),
            'orange_down': os.path.join(self.snakes_dir, 'orange_snake_head_down.png'),
            'orange_right': os.path.join(self.snakes_dir, 'orange_snake_head_right.png'),
            'orange_left': os.path.join(self.snakes_dir, 'orange_snake_head_left.png'),
            'orange_goriz': os.path.join(self.snakes_dir, 'orange_snake_gorizontal.png'),
            'orange_vertical': os.path.join(self.snakes_dir, 'orange_snake_vertical.png'),
            

            'apple_img': os.path.join(self.object_dir, 'apple_img.png'),
            'coin': os.path.join(self.object_dir, 'coin_img.png'),
            'heart_elexir_pin': os.path.join(self.object_dir, 'heart_elexir_pin.png'),
            'shooting_star_pin': os.path.join(self.object_dir, 'shooting_star_pin.png'),

            'eye1': os.path.join(self.static_evil_dir, 'eye1.png'),
            'eye2': os.path.join(self.static_evil_dir, 'eye2.png'),
            'eye3': os.path.join(self.static_evil_dir, 'eye3.png'),
            'eye4': os.path.join(self.static_evil_dir, 'eye4.png'),
            'eye5': os.path.join(self.static_evil_dir, 'eye5.png'),
            'eye6': os.path.join(self.static_evil_dir, 'eye6.png'),
            'eye7': os.path.join(self.static_evil_dir, 'eye7.png'),
            'ezh1': os.path.join(self.static_evil_dir, 'zub_1.png'),
            'ezh2': os.path.join(self.static_evil_dir, 'zub_2.png'),
            'ezh3': os.path.join(self.static_evil_dir, 'zub_3.png'),
            'ezh4': os.path.join(self.static_evil_dir, 'zub_4.png'),
            'ezh5': os.path.join(self.static_evil_dir, 'zub_5.png'),
            'ezh6': os.path.join(self.static_evil_dir, 'zub_6.png'),
            'ezh7': os.path.join(self.static_evil_dir, 'zub_7.png'),
            'ezh8': os.path.join(self.static_evil_dir, 'zub_8.png'),

            'eagle1': os.path.join(self.dynamic_evil_dir, 'eagle_up.png'),
            'eagle2': os.path.join(self.dynamic_evil_dir, 'eagle_down.png'),
            'eagle3': os.path.join(self.dynamic_evil_dir, 'eagle_left.png'),
            'eagle4': os.path.join(self.dynamic_evil_dir, 'eagle_right.png'),
                    }

    def get_name(self, name):
        return self.images.get(name)
    
    def get_sound_name(self, name):
        return self.sound.get(name)

class Dinamik_Evil():
    pass

class Eagle(Dinamik_Evil):
    def __init__(self, settings):
        self.settings = settings
        self.db = settings.db
        self.cell_size = 20
        self.size = 2
        self.position = [5, 5]
        self.path = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_dir = 0
        self.steps = 0
        self.max_steps = 2
        self.images = self.load_images()
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 150 

    def load_images(self):
        images = []
        for key in ['eagle1', 'eagle2', 'eagle4', 'eagle3']:
            path = self.db.get_name(key)
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (40, 40))  # 2x2 клетки
                images.append(img)
        return images

    def update(self):
        dx, dy = self.path[self.current_dir]
        self.position[0] += dx
        self.position[1] += dy
        self.steps += 1

        if self.steps >= self.max_steps:
            self.steps = 0
            self.current_dir = (self.current_dir + 1) % 4
        self.animation_timer += 16

        if self.animation_timer > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.animation_timer = 0

    def draw(self, surface):
        if not self.images:
            return

        x, y = self.position
        px = x * self.cell_size
        py = y * self.cell_size

        surface.blit(self.images[self.current_frame], (px, py))

    def check_collision(self, snake_head):
        x, y = self.position
        eagle_cells = [
            (x, y),
            (x + 1, y),
            (x, y + 1),
            (x + 1, y + 1)
        ]
        return snake_head in eagle_cells

class Static_Evil():
    def __init__(self, settings, image_keys):
        self.settings = settings
        self.db = settings.db

        self.cell_size = 20
        self.grid_width = 16
        self.grid_height = 9

        self.position = (0, 0)

        self.images = self.load_images(image_keys)
        self.current_image = random.choice(self.images)

        self.animation_timer = 0
        self.animation_delay = random.randint(200, 600)  # мс

        self.respawn([])

    def load_images(self, keys):
        images = []
        for key in keys:
            path = self.db.get_name(key)
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (20, 20))
                images.append(img)
        return images

    def respawn(self, snake_body):
        while True:
            pos = (
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)
            )
            if pos not in snake_body:
                self.position = pos
                break

    def update(self):
        self.animation_timer += pygame.time.get_ticks() % 50

        if self.animation_timer > self.animation_delay:
            self.current_image = random.choice(self.images)
            self.animation_timer = 0
            self.animation_delay = random.randint(200, 600)

    def draw(self, surface):
        x, y = self.position
        px = x * self.cell_size
        py = y * self.cell_size

        if self.current_image:
            surface.blit(self.current_image, (px, py))

class Eye(Static_Evil):
    def __init__(self, settings):
        super().__init__(settings, [
            'eye1',
            'eye2',
            'eye3',
            'eye4',
            'eye5',
            'eye6',
            'eye7'
        ])

class Hedhehog(Static_Evil):
    def __init__(self, settings):
        super().__init__(settings, [
            'ezh1',
            'ezh2',
            'ezh3',
            'ezh4',
            'ezh5',
            'ezh6',
            'ezh7',
            'ezh8'
        ])

class Food():
    def __init__(self, settings, image_key):
        self.settings = settings
        self.db = settings.db
        self.cell_size = 20
        self.grid_width = 16
        self.grid_height = 9
        self.position = (0, 0)
        self.image = self.load_image(image_key)
        self.respawn([])

    def load_image(self, image_key):
        path = self.db.get_name(image_key)

        if path and os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (20, 20))
        else:
            print(f"Не найдено изображение: {image_key}")
            return None

    def respawn(self, snake_body):
        while True:
            pos = (
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)
            )

            if pos not in snake_body:
                self.position = pos
                break

    def draw(self, surface):
        x, y = self.position

        px = x * self.cell_size
        py = y * self.cell_size

        if self.image:
            surface.blit(self.image, (px, py))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (px, py, 20, 20))


class Apple(Food):
    def __init__(self, settings):
        super().__init__(settings, 'apple_img')

class Coins(Food):
    def __init__(self, settings):
        super().__init__(settings, 'coin')
        self.active = False

    def try_spawn(self, snake_body):
        if not self.active and random.random() < 0.03:
            self.respawn(snake_body)
            self.active = True

    def collect(self):
        self.active = False



class Snake_Basic:
    def __init__(self, settings, skin='blue' ):
        self.settings = settings
        self.db = settings.db
        self.skin = skin

        self.cell_size = 20
        self.body = [(10, 5), (9, 5), (8, 5)]

        self.direction = (1, 0)
        self.next_direction = self.direction

        self.load_images()

    def load_images(self):
        self.images = {}

        if self.skin == 'default':
            keys = {
                "head_up": 'head_up',
                "head_down": 'head_down',
                "head_left": 'head_left',
                "head_right": 'head_right',
                "body_vertical": 'body_up',
                "body_horizontal": 'body_left'
                }
        else:
            prefix = self.skin
            keys = {
                "head_up": f'{prefix}_up',
                "head_down": f'{prefix}_down',
                "head_left": f'{prefix}_left',
                "head_right": f'{prefix}_right',
                "body_vertical": f'{prefix}_vertical',
                "body_horizontal": f'{prefix}_goriz'
                }

        for name, key in keys.items():
            path = self.db.get_name(key)

            if not path or not os.path.exists(path):
                print(f"[ERROR] Не найдено изображение: {key}")
                continue
            img = pygame.image.load(path).convert_alpha()
            self.images[name] = pygame.transform.scale(img, (20, 20))

    def handle_input(self, key):
        if key == pygame.K_w and self.direction != (0, 1):  
            self.next_direction = (0, -1)
        elif key == pygame.K_s and self.direction != (0, -1):  
            self.next_direction = (0, 1)
        elif key == pygame.K_a and self.direction != (1, 0):  
            self.next_direction = (-1, 0)
        elif key == pygame.K_d and self.direction != (-1, 0): 
            self.next_direction = (1, 0)

    def update(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, surface):

        for i, segment in enumerate(self.body):
            x, y = segment
            px = x * self.cell_size
            py = y * self.cell_size

            if i == 0:
                image = self.get_head_image()
            else:
                image = self.get_body_image(i)

            surface.blit(image, (px, py))

    def get_head_image(self):
        if self.direction == (0, -1):
            return self.images["head_up"]
        elif self.direction == (0, 1):
            return self.images["head_down"]
        elif self.direction == (-1, 0):
            return self.images["head_left"]
        elif self.direction == (1, 0):
            return self.images["head_right"]

    def get_body_image(self, index):
        prev = self.body[index - 1]
        curr = self.body[index]

        if prev[0] == curr[0]:
            return self.images["body_vertical"]
        else:
            return self.images["body_horizontal"]

class Red_Snake(Snake_Basic):
    def __init__(self, settings):
        super().__init__(settings, skin='red')


class Blue_Snake(Snake_Basic):
    def __init__(self, settings):
        super().__init__(settings, skin='blue')


class Yellow_Snake(Snake_Basic):
    def __init__(self, settings):
        super().__init__(settings, skin='yellow')


class Orange_Snake(Snake_Basic):
    def __init__(self, settings):
        super().__init__(settings, skin='orange')


class Purple_Snake(Snake_Basic):
    def __init__(self, settings):
        super().__init__(settings, skin='purple')

SNAKE_CLASSES = {
    'default': Snake_Basic,
    'red': Red_Snake,
    'blue': Blue_Snake,
    'yellow': Yellow_Snake,
    'orange': Orange_Snake,
    'purple': Purple_Snake
}

class Start_Game:
    def __init__(self, window, settings, bg_key=None, fps=10):
        self.window = window
        self.settings = settings
        self.running = True
        self.base_resolution = (320, 180)
        self.game_surface = pygame.Surface(self.base_resolution)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.bg = None
        self.bg_key = bg_key
        self.load_background()
        self.snake = None
        self.apple = None
        self.gmov_menu = Game_Over_Menu
        self.sounds = {}
        self.load_sounds()

    def load_background(self):
        if self.bg_key:
            path = self.settings.db.get_name(self.bg_key)
            if path and os.path.exists(path):
                self.bg = pygame.image.load(path).convert()
            else:
                print(f"Фон не найден: {self.bg_key}")

    def setup(self):
        snake_class = SNAKE_CLASSES.get(
            self.settings.selected_skin,
            Snake_Basic
        )
        self.snake = snake_class(self.settings)

        self.apple = Apple(self.settings)
        self.coin = Coins(self.settings)
        self.eye = Eye(self.settings)
        self.hedgehog = None
        self.eagle = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = True
                    pause_menu = Pause_Menu(self.window, self.settings, self)
                    pause_menu.run()
                self.snake.handle_input(event.key)

    def load_sounds(self):
        def load(name):
            path = self.settings.db.get_sound_name(name)
            if path and os.path.exists(path):
                return pygame.mixer.Sound(path)

        self.sounds['apple'] = load('apple_nom_sound')
        self.sounds['coin'] = load('coin_sound')
        self.sounds['self_hit'] = load('snake_heat_self')
        self.sounds['wall_hit'] = load('snake_heat_border')
        self.sounds['hadgehog_sound'] = load('hadgehog_sound')

    def update(self):
        self.snake.update()
        self.eye.update()
        if self.hedgehog:
            self.hedgehog.update()
        if self.eagle:
            self.eagle.update()

        head = self.snake.body[0]
        x, y = head

        if x < 0 or x >= self.apple.grid_width or y < 0 or y >= self.apple.grid_height:
            self.running = False
            game_over = self.gmov_menu(self.window, self.settings)

            if self.sounds["wall_hit"]:
                self.sounds["wall_hit"].play()
                pygame.time.delay(200)
            game_over.run()
            return

        if head == self.apple.position:
            self.snake.grow()
            self.apple.respawn(self.get_blocked_positions())
            if self.sounds["apple"]:
                self.sounds["apple"].play()

        if head in self.snake.body[1:]:
            self.running = False
            game_over = self.gmov_menu(self.window, self.settings)
            if self.sounds["self_hit"]:
                self.sounds["self_hit"].play()
                pygame.time.delay(200)
            game_over.run()
            return

        if self.eagle and self.eagle.check_collision(self.snake.body[0]):
            self.running = False
            game_over = self.gmov_menu(self.window, self.settings)
            game_over.run()
            return
        
        if self.snake.body[0] == self.eye.position:
            self.running = False
            game_over = self.gmov_menu(self.window, self.settings)
            game_over.run()
            return
        
        if self.hedgehog and self.snake.body[0] == self.hedgehog.position:
            self.running = False
            game_over = self.gmov_menu(self.window, self.settings)

            if self.sounds["hadgehog_sound"]:
                self.sounds["hadgehog_sound"].play()
                pygame.time.delay(200)

            game_over.run()
            return
        
        self.coin.try_spawn(self.snake.body)
        if self.coin.active and head == self.coin.position:
            self.settings.coins.add(1)

            if self.sounds["coin"]:
                self.sounds["coin"].play()
            self.coin.collect()

    def draw(self):

        if self.bg:
            self.game_surface.blit(self.bg, (0, 0))
        else:
            self.game_surface.fill((0, 0, 0))
        self.snake.draw(self.game_surface)
        self.apple.draw(self.game_surface)

        if self.eagle:
            self.eagle.draw(self.game_surface)

        if self.coin.active:
            self.coin.draw(self.game_surface)
        
        if self.hedgehog:
            self.hedgehog.draw(self.game_surface)

        self.eye.draw(self.game_surface)

        font = pygame.font.Font(None, 25)
        text = font.render(f"Coins: {self.settings.coins.amount}", True, (255, 255, 0))
        self.game_surface.blit(text, (5, 5))

        scale_x = self.settings.screen_size[0] // 320
        scale_y = self.settings.screen_size[1] // 180
        scale = min(scale_x, scale_y)
        scaled_surface = pygame.transform.scale(
            self.game_surface,
            (320 * scale, 180 * scale)
        )
        pos_x = (self.settings.screen_size[0] - scaled_surface.get_width()) // 2
        pos_y = (self.settings.screen_size[1] - scaled_surface.get_height()) // 2
        self.window.fill((0, 0, 0))
        self.window.blit(scaled_surface, (pos_x, pos_y))

        pygame.display.flip()
    
    def get_blocked_positions(self):
        blocked = list(self.snake.body)

        if self.eagle:
            x, y = self.eagle.position
            blocked += [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]

        if self.eye:
            blocked.append(self.eye.position)

        if self.hedgehog:
            blocked.append(self.hedgehog.position)
        return blocked

    def run(self):
        self.setup()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(self.fps)
    def play_music(self, key):
        path = self.settings.db.get_sound_name(key)
        if path and os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(self.settings.volume / 100)
            pygame.mixer.music.play(-1)

class Base_Menu():
    def __init__(self, title, window, settings, bg_key=None ):
        self.window = window
        self.settings = settings
        self._bg_image = None
        self.theme = pygame_menu.themes.THEME_DARK.copy()
        self.theme.widget_selection_effect = pygame_menu.widgets.NoneSelection()

        if bg_key:
            path = self.settings.db.get_name(bg_key)
            if path and os.path.exists(path):
                self.theme.background_color = pygame_menu.baseimage.BaseImage(path)

        self.menu = pygame_menu.Menu(
            title,
            1920,
            1080,
            theme=self.theme
            )
    
    def play_music(self, key):
        path = self.settings.db.get_sound_name(key)
        if path and os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(self.settings.volume / 100)
            pygame.mixer.music.play(-1)
    
    def run(self):
        self.menu.mainloop(self.window)

class Main_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Menu', window, settings, bg_key='mm_menu_img')
        self.play_music('mm_sound')
        self.menu.add.button('Play', self.open_lvls)
        self.menu.add.button('Shop', self.open_shop)
        self.menu.add.button('Setting', self.open_stng)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.add.label('v0.1')

    def open_lvls(self):
        Levels = Level_Menu(self.window, self.settings)
        Levels.run()
        self.play_music('mm_sound')
        
    def open_shop(self):
        Shop = Shop_Menu(self.window, self.settings)
        Shop.run()
        self.play_music('mm_sound')

    def open_stng(self):
        Setting = Setting_Menu(self.window, self.settings)
        Setting.run()

class Game_Over_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Game Over', window, settings)
        self.menu.add.label('You Lose!')
        self.menu.add.button('Back', self.menu.disable)
    def lose_or_use_life(self):
        if self.settings.lives > 0:
            self.settings.lives -= 1
            self.settings.save_settings()

            self.snake = Snake_Basic(self.settings)
        else:
            self.lose_or_use_life()

class Level1(Start_Game):
    def __init__(self, window, settings):
        super().__init__(window, settings, bg_key='lvl1_bg', fps=5)

    def setup(self):
        super().setup()
        self.play_music('lvl1_sound')

class Level2(Start_Game):
    def __init__(self, window, settings):
        super().__init__(window, settings, bg_key='lvl2_bg', fps=10)
    
    def setup(self):
        super().setup()
        self.hedgehog = Hedhehog(self.settings)

class Level3(Start_Game):
    def __init__(self, window, settings):
        super().__init__(window, settings, bg_key='lvl3_bg', fps=12)
    
    def setup(self):
        super().setup()
        self.hedgehog = Hedhehog(self.settings)
        self.eagle = Eagle(self.settings)

class Level4(Start_Game):
    def __init__(self, window, settings):
        super().__init__(window, settings, bg_key='lvl4_bg', fps=13)

    def setup(self):
        super().setup()
        self.hedgehog = Hedhehog(self.settings)
        self.eagle = Eagle(self.settings)

class Level5(Start_Game):
    def __init__(self, window, settings):
        super().__init__(window, settings, bg_key='lvl5_bg', fps=15)
    
    def setup(self):
        super().setup()
        self.hedgehog = Hedhehog(self.settings)
        self.eagle = Eagle(self.settings)

class Level_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Levels', window, settings)
        self.menu.add.button('level 1', lambda: self.Start_Level(1))
        self.menu.add.button('level 2', lambda: self.Start_Level(2))
        self.menu.add.button('level 3', lambda: self.Start_Level(3))
        self.menu.add.button('level 4', lambda: self.Start_Level(4))
        self.menu.add.button('level 5', lambda: self.Start_Level(5))
        self.menu.add.button('Back', self.menu.disable)
    
    def Start_Level(self, level):
        inventory = Inventory_Menu(self.window, self.settings)
        inventory.run()

        if level == 1:
            game = Level1(self.window, self.settings)
        elif level == 2:
            game = Level2(self.window, self.settings)
        elif level == 3:
            game = Level3(self.window, self.settings)
        elif level == 4:
            game = Level4(self.window, self.settings)
        elif level == 5:
            game = Level5(self.window, self.settings)
        else:
            return

        game.run()

class Shop_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Shop', window, settings, bg_key='sh_menu_img')
        self.heart_button_rect = pygame.Rect(1620, 930, 300, 150)
        self.play_music('shop_menu_sound')
        self.menu.add.button('Heart Potion', self.open_panel, 'heart', font_color=(255, 0, 0))
        self.menu.add.button('Star', self.open_panel, 'star', font_color=(255, 255, 0))
        self.menu.add.button('snow', font_color=(0, 0, 255))
        self.menu.add.button('Back', self.menu.disable)
        self.menu.set_onupdate(self.draw_coins)
        self.panels = {'heart': self.load_panel('heart_elexir_icon'),
            'star': self.load_panel('Shooting_star_icon')}
        self.active_panel = None
    
    def open_panel(self, panel_type):
        self.active_panel = panel_type
    
    def load_panel(self, key):
        path = self.settings.db.get_name(key)
        if path and os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (1920, 1080))
        return None
    
    def handle_close_panel(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.active_panel = None
    
    def handle_mouse(self, events):  
        if not self.active_panel:
            return

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                mouse_pos = pygame.mouse.get_pos()
  
    def draw_coins(self, *args):
        font = pygame.font.Font(None, 100)
        text = font.render(f"Coins: {self.settings.coins.amount}", True, (255, 255, 0))
        self.window.blit(text, (20, 20))
        self.handle_close_panel()

        if self.active_panel:
            panel = self.panels.get(self.active_panel)
            if panel:
                rect = panel.get_rect(center=(960, 540))
                self.window.blit(panel, rect)

class Effects():
    pass

class User_Coins:
    def __init__(self, settings):
        self.settings = settings
        self.amount = 0
        self.load()

    def load(self):
        if os.path.exists(self.settings.config_path):
            with open(self.settings.config_path, 'r') as f:
                data = json.load(f)
                self.amount = data.get('coins', 0)

    def save(self):
        if os.path.exists(self.settings.config_path):
            with open(self.settings.config_path, 'r') as f:
                data = json.load(f)
        else:
            data = {}

        data['coins'] = self.amount

        with open(self.settings.config_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add(self, value):
        self.amount += value
        self.save()

    def spend(self, value):
        if self.amount >= value:
            self.amount -= value
            self.save()
            return True
        return False

class User_Items():
    pass

class Inventory_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Inventory', window, settings, bg_key=None)
        self.menu.add.label('CHOICE SNAKE:')

        for skin in SNAKE_CLASSES.keys():
            self.menu.add.button(
                skin,
                lambda s=skin: self.select_skin(s)
            )
        self.menu.add.button('READY', self.menu.disable)

    def select_skin(self, skin):
        self.settings.selected_skin = skin
        self.settings.save_settings()

class Setting_Menu(Base_Menu):
    def __init__(self, window, settings):
        super().__init__('Settings', window, settings, bg_key='st_menu_img')
        self.menu.add.range_slider(
            'Громкость: ',
            default=settings.volume, 
            range_values=(0, 100),
            increment=1,
            value_format=lambda x: f'{int(x)}%',
            onchange=self.change_volume)
        self.menu.add.button('Back', self.menu.disable)
    
    def change_volume(self, value):
        self.settings.volume = int(value)
        pygame.mixer.music.set_volume(self.settings.volume / 100)
        self.settings.save_settings()

class Pause_Menu(Base_Menu):
    def __init__(self, window, settings, game):
        super().__init__('Pause', window, settings)
        self.game = game
        self.menu.add.label('Paused')
        self.menu.add.button('Continue', self.resume)
        self.menu.add.button('Main Menu', self.exit_to_menu)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def resume(self):
        self.game.paused = False
        self.menu.disable()

    def exit_to_menu(self):
        self.game.running = False
        self.menu.disable()

if __name__ == "__main__":
    stng = Data_Setting()
    main_window = pygame.display.set_mode(stng.screen_size)
    music_path = stng.db.get_sound_name('mm_sound')

    if music_path and os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(stng.volume / 100)
        pygame.mixer.music.play(-1)

    app = Main_Menu(main_window, stng)
    app.run()