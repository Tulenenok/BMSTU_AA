screen_t *screen;                                                                   // (1)
std::vector<triangle_t*> triangles;                                                 // (2)
screen.init();                                                                      // (3)
triangles.init();                                                                   // (4)

for (int y = screen->height - 1; y >= 0; y--){                                      // (5)

    if (y < screen->height && y >= 0) {                                             // (6)
    
        auto *depth_array = (double*) malloc(sizeof(double) * screen->width);       // (7)

        for (int i = 0; i < screen->width; i++) {                                   // (8)
    
            depth_array[i] = 1e33;                                                  // (9)
    
        }

        for (int i = 0; i < triangles.size(); i++) {                                // (10)
    
            process_level(triangles[i], screen, y, depth_array);                    // (11)       
    
        }

        for (int x = 0; x < screen->width; x++) {                                   // (12)
    
            if (not screen->change[x][y] && depth_array[x] == INT_MAX) {            // (13)
    
                color_pixel(screen, &(screen->default_color), x, y);                // (14)
    
            }
        }

        free(depth_array);                                                          // (15)
    }
}

screen.set_all_pixel_true();                                                        // (16)
screen.convert();                                                                   // (17)
screen.show();                                                                      // (18)
screen.set_all_pixel_false();                                                       // (19)
screen.free()                                                                       // (20)
triangles.free()                                                                    // (21)