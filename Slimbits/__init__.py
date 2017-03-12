from PIL import Image, ImageDraw
import random


class Slimbit:
    def __init__(self, size):
        # save tru size and scale size up for drawing
        self.true_size = size
        self.size = size * 4
        # Get portions
        self.grid = self.grid_list()
        self.lines = self.line_list()
        self.fill = (0, 0, 0)
        
    
    def draw_lines(self, slimbit, density):
        line_width = int(self.size / 60)
        draw = ImageDraw.Draw(slimbit)
        random.shuffle(self.lines)
        for i in range(0, density):
            draw.line(self.lines[i], fill=0, width=line_width)
    
    def draw_grid(self, slimbit):
        draw = ImageDraw.Draw(slimbit) # Create a draw object
        for point in self.grid:
            # Draw a circle
            draw.ellipse(point, fill=0)
    
    def create(self, density):
        density = density if density < 28 else 28
        size = self.size
        # Create white box
        slimbit = Image.new('RGB', (size, size), (255, 255, 255))
        self.draw_grid(slimbit)
        
        self.draw_lines(slimbit, density)
        
        # Scale back down
        slimbit = slimbit.resize((self.true_size, self.true_size), Image.LANCZOS)
        return slimbit
        
    def grid_list(self):
        i = self.size / 4 #  Incrementor
        r = self.size / 48 #  Radius
        return [
            # Top Row
            ((i * 1) - r, (i * 1) - r, (i * 1) + r, (i * 1) + r),
            ((i * 2) - r, (i * 1) - r, (i * 2) + r, (i * 1) + r),
            ((i * 3) - r, (i * 1) - r, (i * 3) + r, (i * 1) + r),
            # Middle Row
            ((i * 1) - r, (i * 2) - r, (i * 1) + r, (i * 2) + r),
            ((i * 2) - r, (i * 2) - r, (i * 2) + r, (i * 2) + r),
            ((i * 3) - r, (i * 2) - r, (i * 3) + r, (i * 2) + r),
            # Bottom Row
            ((i * 1) - r, (i * 3) - r, (i * 1) + r, (i * 3) + r),
            ((i * 2) - r, (i * 3) - r, (i * 2) + r, (i * 3) + r),
            ((i * 3) - r, (i * 3) - r, (i * 3) + r, (i * 3) + r),
        ]
    
        
    def line_list(self):
        i = self.size / 4 #  Incrementor
        return [
        	[(i * 3, i * 2), (i * 1, i * 1)],
        	[(i * 3, i * 3), (i * 1, i * 2)],
        	[(i * 1, i * 3), (i * 3, i * 2)],
        	[(i * 1, i * 2), (i * 3, i * 1)],
        	[(i * 2, i * 1), (i * 1, i * 3)],
        	[(i * 3, i * 1), (i * 2, i * 3)],
        	[(i * 2, i * 1), (i * 3, i * 3)],
        	[(i * 1, i * 1), (i * 2, i * 3)],
        	[(i * 2, i * 3), (i * 3, i * 2)],
        	[(i * 1, i * 3), (i * 2, i * 2)],
        	[(i * 2, i * 2), (i * 3, i * 1)],
        	[(i * 1, i * 2), (i * 2, i * 1)],
        	[(i * 2, i * 2), (i * 3, i * 3)],
        	[(i * 1, i * 2), (i * 2, i * 3)],
        	[(i * 2, i * 1), (i * 3, i * 2)],
        	[(i * 1, i * 1), (i * 2, i * 2)],
        	[(i * 3, i * 3), (i * 3, i * 2)],
        	[(i * 2, i * 3), (i * 2, i * 2)],
        	[(i * 1, i * 3), (i * 1, i * 2)],
        	[(i * 3, i * 2), (i * 3, i * 1)],
        	[(i * 2, i * 2), (i * 2, i * 1)],
        	[(i * 1, i * 2), (i * 1, i * 1)],
        	[(i * 2, i * 3), (i * 3, i * 3)],
        	[(i * 1, i * 3), (i * 2, i * 3)],
        	[(i * 2, i * 2), (i * 3, i * 2)],
        	[(i * 1, i * 2), (i * 2, i * 2)],
        	[(i * 2, i * 1), (i * 3, i * 1)],
        	[(i * 1, i * 1), (i * 2, i * 1)],
        ]
