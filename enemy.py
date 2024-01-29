class Enemy(pygame.sprite.Sprite):  # класс для создания космической тарелки
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load('graphics/enemy.png')
        self.screen_width = screen_width
        self.screen_height = screen_height
        x = random.choice([0, screen_width - self.image.get_width()])
        if x == 0:
            self.speed = 5
        else:
            self.speed = -5
        self.rect = self.image.get_rect(topleft=(x, 40))
        self.bullets_group = pygame.sprite.Group()
        self.bullets_ready = True
        self.bullets_time = 0
        self.bullet_recharge = 250
        self.bullet_music = pygame.mixer.Sound('music/bullet_music.mp3')

    def kills(self):
        if self.bullets_ready:
            self.bullets_ready = False
            bullet = Bullet(self.screen_width, self.screen_height - 200, self.rect.x + self.image.get_width() / 2,
                            self.rect.y + self.image.get_height())
            self.bullets_group.add(bullet)
            self.bullet_music.play()

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed = -self.speed

        self.bullets_group.update()
        for bullet in self.bullets_group:
            if bullet.rect.colliderect(self.rect):
                bullet.kill()
                self.kill()
