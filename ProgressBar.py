import pygame

class ProgressBar:
    def __init__(self,
        maximum: int,
        current: int,
        top_left: tuple[int,int],
        length: int,
        height: int,                
    ) -> None:
        
        # Health values
        self.max_health: int = maximum
        self.current_health: int = current
        self.percentage: float = self.current_health / self.max_health
        
        # Animation
        self.animation_speed: int = 1
        self.animation_queue: list[int] = []
        
        # Positioning
        if height > 20:
            self.height: int = height
        else:
            raise Exception('"height" must be greater the 16')
        if length > 20:
            self.length: int = length
        else: 
            raise Exception('"length" must be greater the 16')
        self.top_left: tuple[int,int] = top_left
        
        # Graphics
        self.outer_rect = pygame.Rect(top_left[0],top_left[1],length,height)
        self.filler_rect = pygame.Rect(top_left[0]+8,top_left[1]+8,length-16,(height)-16)
        self.bar_rect = pygame.Rect(top_left[0]+8,top_left[1]+8,round(length*self.percentage)-16,(height)-16)
        self.bar_colour: str = '#2BA84A' # Default green, gets overwritten immediatly
    
    
    def update_bar_colour(self) -> None:
        if self.percentage <= 0.25:
            self.bar_colour = '#FF331F'
        elif self.percentage <= 0.5:
            self.bar_colour = '#FFA62B'
        else:
            self.bar_colour = '#2BA84A'
        

    def add_bar_queue(self,val:int):
        self.animation_queue.append(val)        

    def update_bar(self):
        if self.animation_queue == []:
            return
        
        if self.animation_queue[0] > 0:
            if self.animation_queue[0] <= self.animation_speed:
                self.current_health += self.animation_queue[0]
                self.animation_queue.pop(0)
                
            else:
                self.animation_queue[0] -= self.animation_speed
                self.current_health += self.animation_speed
                
        else:
            if self.animation_queue[0] >= self.animation_speed* -2:
                self.current_health += self.animation_queue[0]
                self.animation_queue.pop(0)
                
            else:
                self.animation_queue[0] += self.animation_speed
                self.current_health -= self.animation_speed
            
    def update_percentage(self) -> None:
        self.percentage = self.current_health / self.max_health


    def display(self,screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, '#2F2F2F', self.outer_rect)
        pygame.draw.rect(screen, '#FAF6ED', self.filler_rect)
        # Rerenders the Rect with new percentage
        self.bar_rect = pygame.Rect(self.top_left[0]+8,self.top_left[1]+8,round(self.length*self.percentage)-16,(self.height)-16)
        pygame.draw.rect(screen, self.bar_colour, self.bar_rect)


    def update(self,screen:pygame.Surface):
        self.update_bar()
        self.update_percentage()
        self.update_bar_colour()
        self.display(screen)