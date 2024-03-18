# DANCEY PANTS REVOLUTION v1.0 == [FULLY MODULAR SCRIPT]  >>>  Written by Rimscar

default persistent.rhythm_dark = False
default persistent.rhythm_difficulty = 1
default persistent.rhythm_highscores = None

image bgrhythm arcade_dark = "mod_assets/rhythm/arcade_dark.jpg" #CREDIT: Minikle [QUUN PLANT Co., Ltd.]
image bgrhythm arcade = "mod_assets/rhythm/arcade.jpg" #CREDIT: Minikle [QUUN PLANT Co., Ltd.]

# Does the heavy lifting FOR YOU! Loops between rhythm_game_menu and rhthm_game
label rhythm_game_loop:
    $ renpy.checkpoint()
    $ renpy.block_rollback()

    $ config.mouse_hide_time = None

    if persistent.rhythm_dark:
        scene bgrhythm arcade_dark
    else:
        scene bgrhythm arcade
    call screen rhythm_game_menu(DPRev.screen_to_save)
    $ request_song, menu_pos = _return
    $ DPRev.screen_pos = menu_pos
    if isinstance(request_song, tuple):
        call screen rhythm_game(
            request_song[2], # path_song
            request_song[3], # path_beatmap
            request_song[0], # title
            persistent.rhythm_difficulty,
            request_song[4] # Chibi
        )
        $ score, max_score, score_format_comma, score_format_k, menu_pos = _return
        $ DPRev.screen_pos = menu_pos
        $ DPRev.screen_to_save = (request_song[0], score, persistent.rhythm_difficulty) # title / score
        jump rhythm_game_loop

    if request_song == True:
        jump rhythm_game_loop
    
    $ quick_menu = True
    return

# Enter main menu of rhythm game, and pick a song or exit
screen rhythm_game_menu(to_save=None):
    default rgm = DPRev.RhythmGameMenu(to_save)
    
    if rgm.request_exit == False:
        if persistent.rhythm_dark:
            default menu_bg = DPRev.Shared.LoopingImage("gui/menu_bg.png", x=DPRev.screen_pos[0], y=DPRev.screen_pos[1], recolor_black="#2E4354", recolor_white="#121413")
            add menu_bg
            add Image("mod_assets/rhythm/gui/mask_dark.png")
        else:
            default menu_bg = DPRev.Shared.LoopingImage("gui/menu_bg.png", x=DPRev.screen_pos[0], y=DPRev.screen_pos[1])
            add menu_bg
            add Image("mod_assets/rhythm/gui/mask.png")
        add Image("mod_assets/rhythm/gui/stage.png", xalign=0.23, yalign=1.0)
        add Image("mod_assets/rhythm/gui/stage_screen.png", xalign=0.27, yalign=0.39)
        if persistent.rhythm_dark:
            add Image('mod_assets/rhythm/gui/book_dark.png', xalign=0.757, yalign=1.0)
            add Image('mod_assets/rhythm/gui/logo_dark.png', xalign=0.24, yalign=0.12)
        else:
            add Image('mod_assets/rhythm/gui/book.png', xalign=0.757, yalign=1.0)
            add Image('mod_assets/rhythm/gui/logo.png', xalign=0.24, yalign=0.12)
        add Image("mod_assets/rhythm/gui/frame.png", xalign=0.5, yalign=1.0)

        text "Setlist":
            color "#fff"
            outlines [(2, '#000', 0, 0)]
            xpos 842 ypos 89
            xalign 0.5 yalign 0.0
            size 48
            font DPRev.get_score_font()
        text rgm.get_difficulty_text():
            xpos 410 ypos 290
            xalign 0.5 yalign 0.5
            size DPRev.get_score_font_size()
            color rgm.get_difficulty_color()
            font DPRev.get_score_font()

        add rgm
    
    if rgm.request_song:
        timer 0.01 action Return((
            rgm.request_song, menu_bg.get_pos()
            ))
    if rgm.request_exit:
        timer 1.0 action Return(
            ( _, (0, -100))
        )
    if rgm.request_redraw:
        timer 0.01 action Return(
            ( True, menu_bg.get_pos()) # Fudge: Yeah we're setting the first value to true just to let the user know we want redraw!
        )

# Enter Rhythm game directly
screen rhythm_game(audio_path, beatmap_path, song_title, difficulty=2, chibi_names=[]):
    default rgd = DPRev.RhythmGame(audio_path, beatmap_path, difficulty, chibi_names)

    if persistent.rhythm_dark:
        default menu_bg = DPRev.Shared.LoopingImage("gui/menu_bg.png", x=DPRev.screen_pos[0], y=DPRev.screen_pos[1], recolor_black="#2E4354", recolor_white="#121413")
        add menu_bg
        add Image("mod_assets/rhythm/gui/mask_dark.png")
    else:
        default menu_bg = DPRev.Shared.LoopingImage("gui/menu_bg.png", x=DPRev.screen_pos[0], y=DPRev.screen_pos[1])
        add menu_bg
        add Image("mod_assets/rhythm/gui/mask.png")
    add Image("mod_assets/rhythm/gui/stage.png", xalign=0.23, yalign=1.0)
    add Image("mod_assets/rhythm/gui/stage_screen.png", xalign=0.27, yalign=0.39)
    if persistent.rhythm_dark:
        add Image('mod_assets/rhythm/gui/book2_dark.png', xalign=0.757, yalign=1.0)
        add Image('mod_assets/rhythm/gui/logo_dark.png', xalign=0.24, yalign=0.12)
    else:
        add Image('mod_assets/rhythm/gui/book2.png', xalign=0.757, yalign=1.0)
        add Image('mod_assets/rhythm/gui/logo.png', xalign=0.24, yalign=0.12)
    add Image("mod_assets/rhythm/gui/frame.png", xalign=0.5, yalign=1.0)   
    
    text str(rgd.combo):
        xpos 688
        xalign 0.4 yalign 0.125
        size 46
        font "gui/font/m1.ttf"
    text song_title:
        xpos 842 ypos 82
        xalign 0.5 yalign 0.0
        size 46
        xmaximum 220
        font "gui/font/m1.ttf"
    text str(rgd.num_hits):
        xalign 0.798 yalign 0.125
        size 46
        font "gui/font/m1.ttf"
    text str(int(rgd.score)):
        xpos 410 ypos 290
        xalign 0.5 yalign 0.5
        size rgd.score_text_size
        color rgd.score_text_color
        font DPRev.get_score_font()

    add rgd

    if rgd.has_ended:
        # use a timer so the player can see the screen before it returns
        timer 2.0 action Return(
            (rgd.score, rgd.get_max_score(difficulty), rgd.get_formatted_score(), rgd.get_formatted_score_k(), menu_bg.get_pos())
        )

init python:

    import os
    import pygame

    class DPRev:

        # Used by external screens / labels Only
        screen_pos = (0, -100)
        screen_to_save = None

        @staticmethod
        def font_linkin():
            return "mod_assets/rhythm/font/LinkinPark-RifficFree-Bold.ttf"

        @staticmethod
        def font_comic():
            return "mod_assets/rhythm/font/ComicZine-XgGa.ttf"

        @staticmethod
        def get_score_font():
            return DPRev.font_linkin() if persistent.rhythm_dark == False else DPRev.font_comic()
        
        @staticmethod
        def get_score_font_size():
            return 32 if persistent.rhythm_dark == False else 48

        @staticmethod
        def floor(n):
            return int(n // 1)

        @staticmethod
        def ceil(n):
            return int(-1 * n // 1 * -1)

        # Shared library classes used by DPRev
        class Shared:

            ## Included for modularity, borrowed from DDLC MOD TEMPLATE 2.0 (by Azariel Del Carmen [GanstaKingofSA]) ===
            #
            # This recolor function allows you to recolor the GUI of DDLC easily without replacing
            # the in-game assets.
            #
            # Syntax to use: recolorize("path/to/your/image", "#color1hex", "#color2hex", contrast value)
            # Example: recolorize("gui/menu_bg.png", "#bdfdff", "#e6ffff", 1.25)
            def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
                return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), 
                    im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

            ## Included for modularity, borrowed from DDLC MOD TEMPLATE 2.0 (by Azariel Del Carmen [GanstaKingofSA]) ===
            #
            # This class handles Chibi Movement in a better way
            class ChibiTrans2(object):
                def __init__(self):
                    self.charTime = renpy.random.random() * 4 + 4
                    self.charPos = 0
                    self.charOffset = 0
                    self.charZoom = 1

                def produce_random(self):
                    return renpy.random.random() * 4 + 4

                def reset_trans(self):
                    self.charTime = self.produce_random()
                    self.charPos = 0
                    self.charOffset = 0
                    self.charZoom = 1

                def randomPauseTime(self, trans, st, at):
                    if st > self.charTime:
                        self.charTime = self.produce_random()
                        return None
                    return 0

                def randomMoveTime(self, trans, st, at):
                    if st > .16:
                        if self.charPos > 0:
                            self.charPos = renpy.random.randint(-1,0)
                        elif self.charPos < 0:
                            self.charPos = renpy.random.randint(0,1)
                        else:
                            self.charPos = renpy.random.randint(-1,1)
                        if trans.xoffset * self.charPos > 5: self.charPos *= -1
                        return None
                    if self.charPos > 0:
                        trans.xzoom = -1
                    elif self.charPos < 0:
                        trans.xzoom = 1
                    trans.xoffset += .16 * 10 * self.charPos
                    self.charOffset = trans.xoffset
                    self.charZoom = trans.xzoom
                    return 0

            # Compact class for rendering chibi's through python
            # EXAMPLE:
            # 1. chibi_s = DPRev.Shared.Chibi('gui/poemgame/s_sticker_1.png', 'gui/poemgame/s_sticker_2.png')
            # 2. chibi_s.render(render, st, at)
            # 3. chibi_s.jump(st)
            class Chibi(ChibiTrans2):
                def __init__(self, image_path, image_path_hop, x=350, y=config.screen_height*.72):
                    super().__init__()

                    # CONFIG
                    self.delay_mod = 0.3
                    self.x_lerp_max_dist = 15
                    self.x_lerp_duration = .2
                    self.y_height = -15
                    self.y_lerp_duration = 0.08
                    self.jump_height = -80
                    self.jump_lerp_duration = .18
                    self.jump_cooldown = 1.0

                    self.sticker = Image(image_path)
                    self.sticker_hop = Image(image_path_hop)
                    self.initial_x = x
                    self.initial_y = y
                    self.charTime = self.charTime*self.delay_mod # override
                    self.cached_char_pos = 0
                    self.cached_time_x = 0
                    self.cached_time_y = 0
                    self.cached_x_offset = 0
                    self.cached_y_offset = 0
                    self.y_target = 0
                    self.is_jumping = False
                    self.jump_queue = 0
                    self.jump_cached_time = 0

                def render(self, render, st, at):

                    # flip if facing right
                    sticker_flipped = self.sticker
                    sticker_hop_flipped = self.sticker_hop
                    if self.charPos > 0 or (self.charPos == 0 and self.cached_char_pos == -1):
                        sticker_flipped = im.Flip(self.sticker, horizontal=True)
                        sticker_hop_flipped = im.Flip(self.sticker_hop, horizontal=True)
                    sticker_transform = Transform(sticker_flipped, zoom=self.charZoom)
                    sticker_hop_transform = Transform(sticker_hop_flipped, zoom=self.charZoom)

                    # move horizontally
                    if st > self.charTime and not self.is_jumping:
                        self.cached_time_x = st
                        self.cached_time_y = st
                        self.cached_char_pos = self.charPos
                        self.cached_x_offset = self.charPos*self.x_lerp_max_dist
                        self.randomMoveTime(sticker_transform, st, at)

                        # do a little jop
                        self.y_target = self.y_height
                    
                    self.randomPauseTime(sticker_transform, st, at)
                    time_elapsed_x = st - self.cached_time_x
                    time_elapsed_y = st - self.cached_time_y

                    # x_offset / y_offset
                    x_lerp_value = min(time_elapsed_x / self.x_lerp_duration, 1.0)
                    x_offset = self.cached_x_offset + x_lerp_value * (self.charPos * self.x_lerp_max_dist - self.cached_x_offset)
                    height = self.jump_height if self.is_jumping == True else self.y_height
                    lerp_duration = self.jump_lerp_duration if self.is_jumping == True else self.y_lerp_duration
                    y_offset = self.update_y(time_elapsed_y, st, height, lerp_duration)

                    sticker = sticker_hop_transform if self.is_jumping == True else sticker_transform
                    render.place(sticker, x=self.initial_x+x_offset, y=self.initial_y+y_offset)

                # Calling this method will initiate a jump
                def jump(self, st, jump_queue=2):
                    if st - self.jump_cached_time < self.jump_cooldown:
                        return
                    self.jump_queue = jump_queue
                    self.jump_helper(st)

                def jump_helper(self, st):
                    self.jump_queue -= 1
                    self.is_jumping = True
                    self.reset_char_time(st)
                    self.cached_time_y = st
                    self.y_target = self.jump_height
                    self.jump_cached_time = st

                def randomPauseTime(self, trans, st, at):
                    if st > self.charTime:
                        self.reset_char_time(st)
                        return None
                    return 0

                def reset_char_time(self, st):
                    self.charTime = self.delay_mod*self.produce_random()+st

                def update_y(self, time_elapsed_y, st, height, lerp_duration):
                    # Calculate lerp value based on time_elapsed_y
                    # y_lerp_value = min(time_elapsed_y / lerp_duration, 1.0)  # Ensure y_lerp_value is between 0 and 1
                    if self.y_target == height:
                        y_lerp_value = min(self.ease_in(time_elapsed_y / lerp_duration), 1.0)
                    else:
                        y_lerp_value = min(self.ease_out(time_elapsed_y / lerp_duration), 1.0)

                    if self.y_target == height:
                        # Interpolate y_offset to y_target (self.y_height)
                        y_offset = y_lerp_value * self.y_target
                        if y_lerp_value == 1.0:
                            self.y_target = 0
                            self.cached_time_y = st
                            self.cached_y_offset = y_offset
                    else:
                        # Interpolate y_offset to 0
                        y_offset = (1-y_lerp_value) * self.cached_y_offset
                        if y_lerp_value == 1.0:
                            self.cached_y_offset = 0
                            if self.jump_queue > 0:
                                self.jump_helper(st)
                            else:
                                self.is_jumping = False
                    return y_offset

                def ease_in(self, t):
                    return pow(t, .5)
                
                def ease_out(self, t):
                    return pow(t, 2)

            # Rewrite of the 'looping image' label in python
            class LoopingImage(renpy.Displayable):
                def __init__(self, image_path, x=0, y=0, vx=-.5, vy=.5, loop_dist=100, recolor_black=None, recolor_white=None):
                    super(DPRev.Shared.LoopingImage, self).__init__()

                    self.image = Transform(image_path)
                    if recolor_black != None and recolor_white != None:
                        self.image = DPRev.Shared.recolorize(image_path, recolor_black, recolor_white, 1)
                    self.x_initial = x
                    self.y_initial = y
                    self.x = x
                    self.y = y
                    self.vx = vx
                    self.vy = vy
                    self.loop_dist = loop_dist

                    # 120 fps only if the monitor supports it, else use 60 fps
                    self.frame_time = 0.0083333 if renpy.get_refresh_rate() >= 115 else 0.0166666

                    self.drawables = [
                        self.image,
                    ]
                    self.cached_time = 0
                
                def render(self, width, height, st, at):
                    render = renpy.Render(width, height)

                    elapsed_time = st - self.cached_time

                    if elapsed_time > self.frame_time:
                        self.x += self.vx
                        self.y += self.vy
                        self.cached_time = st

                    if abs(self.x_initial-self.x) > self.loop_dist or abs(self.y_initial-self.y) > self.loop_dist:
                        self.x = self.x_initial
                        self.y = self.y_initial

                    render.place(self.image, x=self.x, y=self.y)

                    renpy.redraw(self, 0)
                    return render

                def visit(self):
                    return self.drawables

                def get_pos(self):
                    x = (self.x % -self.loop_dist) - self.loop_dist if self.x < 0 else self.x % self.loop_dist
                    y = (self.y % -self.loop_dist) - self.loop_dist if self.y < 0 else self.y % self.loop_dist
                    return (x, y)

        # Menu for selecting songs to play in RhythmGame
        class RhythmGameMenu(renpy.Displayable):
            def __init__(self, to_save=None):
                super(DPRev.RhythmGameMenu, self).__init__()

                pygame.mouse.set_visible(True)

                # Not configurable, don't touch!
                self.request_song = None
                self.request_exit = False
                self.request_redraw = False
                self.hover_index = -1
                self.cached_tracklist_hover = -1
                self.allow_hover_sound = True

                # The actual config starts here:
                self.difficulties = {
                    0: ("EASY", '#fff'),
                    1: ("NORMAL", '#fff'),
                    2: ("HARD", '#fff'),
                    3: ("EXPERT", '#CE0000')
                }

                self.chibi_name_map = {
                    "S": "Sayori",
                    "N": "Natsuki",
                    "Y": "Yuri",
                    "M": "Monika"
                }

                # save latest score
                if to_save != None: # title, score, difficulty
                    self.save_score(to_save[0], DPRev.floor(to_save[1]), to_save[2])

                # self.delete_all_data()

                self.setlist = self.read_setlist_file('rhythm/setlist.txt')
                self.setlist_x = config.screen_width/2+31
                self.setlist_y = config.screen_height*.247
                self.setlist_spacing = 91.5
                self.hover_width = 352
                self.hover_height = 92
                self.star_color = '#FFD800'
                self.icon_r = 16
                self.difficulty_buttons_y = config.screen_height*.534
                self.dark_mode_button_pos = (config.screen_width*.236+80, config.screen_height*.92)
                self.dark_mode_button_hover = False
                self.exit_button_pos = (config.screen_width*.236+123, config.screen_height*.92)
                self.exit_button_hover = False
                self.difficulty_buttons_hover = { 0: False, 1: False, 2: False, 3: False }

                # drawables
                self.hover_rect = Solid('#00ffff15', xsize=self.hover_width, ysize=self.hover_height, alpha=.5)
                self.hover_rect_dark = Solid('#ffffff20', xsize=self.hover_width, ysize=self.hover_height, alpha=.5)
                self.difficulty_button_blank = Image('mod_assets/rhythm/gui/icon_blank.png')
                self.difficulty_buttons = {
                    0: Image('mod_assets/rhythm/gui/icon_s.png'),
                    1: Image('mod_assets/rhythm/gui/icon_n.png'),
                    2: Image('mod_assets/rhythm/gui/icon_y.png'),
                    3: Image('mod_assets/rhythm/gui/icon_m.png')
                }
                self.difficulty_buttons_h = {
                    0: Image('mod_assets/rhythm/gui/icon_s_h.png'),
                    1: Image('mod_assets/rhythm/gui/icon_n_h.png'),
                    2: Image('mod_assets/rhythm/gui/icon_y_h.png'),
                    3: Image('mod_assets/rhythm/gui/icon_m_h.png')
                }
                self.dark_mode_button = Image('mod_assets/rhythm/gui/icon_moon.png')
                self.dark_mode_button_h = Image('mod_assets/rhythm/gui/icon_moon_h.png')
                self.exit_button = Image("mod_assets/rhythm/gui/icon_rect.png")
                self.exit_button_h = Image("mod_assets/rhythm/gui/icon_rect_h.png")
                self.exit_text = Text('EXIT', font=DPRev.font_comic(), xalign=.5, yalign=.5, color='#CE0000', size=30)
                self.stars_images = [Image(f'mod_assets/rhythm/gui/stars/{i}.png') for i in range(1, 11)]

                if persistent.rhythm_dark:
                    self.stars_images = [DPRev.Shared.recolorize(image, '#fff', '#fff') for image in self.stars_images]

                sl_num = 0
                self.sl_text = []
                for set in self.setlist: # song name, artist, song path, beatmap path

                    # color in some of the stars
                    new_stars = self.get_recolored_stars(self.get_score(set[0]))

                    self.sl_text.append( (
                        sl_num, 
                        Text(set[0], xalign=0, yalign=0, size=46, font="gui/font/m1.ttf", 
                            color='#fff', outlines=[(2, '#000000b0', 0, 0)]), # Title
                        Text(set[1], xalign=0, yalign=0, size=16, font=DPRev.font_linkin(), 
                            color='#fff', outlines=[(2, '#000000b0', 0, 0)]), # Artist
                        Text(self.get_formatted_score(set[0]), xalign=1.0, yalign=0, size=16, font=DPRev.font_linkin(), 
                            color='#fff', outlines=[(2, '#000000b0', 0, 0)]), # Highscore
                        new_stars
                        ) )
                    sl_num += 1

                # Visit order
                self.drawables = [
                    self.hover_rect,
                    self.hover_rect_dark,
                    self.difficulty_button_blank,
                    self.dark_mode_button,
                    self.dark_mode_button_h,
                    self.exit_button,
                    self.exit_button_h,
                    self.exit_text,
                ]
                self.drawables.extend(list(self.difficulty_buttons.values()))
                self.drawables.extend(list(self.difficulty_buttons_h.values()))
            
            # Create renpy object with width & height parameters
            def render(self, width, height, st, at):
                render = renpy.Render(width, height)

                # difficulty buttons
                for button_id in self.difficulty_buttons:
                    if self.difficulty_buttons_hover[button_id]:
                        render.place(self.difficulty_buttons_h[button_id], x=config.screen_width*.236 + button_id*60, y=self.difficulty_buttons_y)
                    else:
                        if button_id == persistent.rhythm_difficulty:
                            render.place(self.difficulty_buttons[button_id], x=config.screen_width*.236 + button_id*60, y=self.difficulty_buttons_y)
                        else:
                            render.place(self.difficulty_button_blank, x=config.screen_width*.236 + button_id*60, y=self.difficulty_buttons_y)

                # dark mode button
                if self.dark_mode_button_hover:
                    render.place(self.dark_mode_button_h, x=self.dark_mode_button_pos[0], y=self.dark_mode_button_pos[1])
                else:
                    render.place(self.dark_mode_button, x=self.dark_mode_button_pos[0], y=self.dark_mode_button_pos[1])

                # exit button
                if self.exit_button_hover:
                    render.place(self.exit_button_h, x=self.exit_button_pos[0], y=self.exit_button_pos[1])
                else:
                    render.place(self.exit_button, x=self.exit_button_pos[0], y=self.exit_button_pos[1])
                render.place(self.exit_text, x=-165, y=319)

                # tracklist select            
                if self.hover_index >= 0:
                    if persistent.rhythm_dark:
                        render.place(self.hover_rect_dark, x=self.setlist_x, y=self.setlist_y + self.hover_index*self.hover_height)
                    else:
                        render.place(self.hover_rect, x=self.setlist_x, y=self.setlist_y + self.hover_index*self.hover_height)

                spacing = 91.5
                for text in self.sl_text:
                    render.place(text[1], x=config.screen_width*.535, y=config.screen_height*.241 + spacing*text[0])
                    render.place(text[2], x=config.screen_width*.55, y=config.screen_height*.32 + spacing*text[0])
                    render.place(text[3], x=-config.screen_width*.21, y=config.screen_height*.32 + spacing*text[0])

                    # Stars
                    s_index = 0
                    for star in text[4]:
                        render.place(star, x=config.screen_width*.745+s_index*23, y=config.screen_height*.27 + spacing*text[0])
                        s_index += 1

                renpy.redraw(self, 0)
                return render

            def event(self, ev, x, y, st):

                allow_hover_counter = 0

                # cursor is over other menu options
                for button_id in self.difficulty_buttons:
                    if self.is_in_radius(x, y, config.screen_width*.236 + button_id*60, self.difficulty_buttons_y, self.icon_r):
                        self.difficulty_buttons_hover[button_id] = True
                        if self.allow_hover_sound:
                            renpy.play("gui/sfx/hover.ogg")
                            self.allow_hover_sound = False
                    else:
                        self.difficulty_buttons_hover[button_id] = False
                        allow_hover_counter += 1
                
                if self.is_in_radius(x, y, self.dark_mode_button_pos[0], self.dark_mode_button_pos[1], self.icon_r):
                    self.dark_mode_button_hover = True
                    if self.allow_hover_sound:
                        renpy.play("gui/sfx/hover.ogg")
                        self.allow_hover_sound = False
                else:
                    self.dark_mode_button_hover = False
                    allow_hover_counter += 1
                
                if x > self.exit_button_pos[0] and x < self.exit_button_pos[0]+self.icon_r*6 and y > self.exit_button_pos[1] and x < self.exit_button_pos[1]+self.icon_r:
                    self.exit_button_hover = True
                    if self.allow_hover_sound:
                        renpy.play("gui/sfx/hover.ogg")
                        self.allow_hover_sound = False
                else:
                    self.exit_button_hover = False
                    allow_hover_counter += 1

                # a large hover counter means our cursor is not over any object
                if allow_hover_counter >= 6:
                    self.allow_hover_sound = True

                # is cursor hovering over setlist
                if y > self.setlist_y and x > self.setlist_x and x < self.setlist_x+self.hover_width:
                    diff = (y-self.setlist_y) / self.hover_height
                    diff = DPRev.floor(diff)
                    if diff < len(self.setlist):
                        self.hover_index = diff
                        if diff != self.cached_tracklist_hover:
                            renpy.play("gui/sfx/hover.ogg")
                            self.cached_tracklist_hover = diff
                    else:
                        self.hover_index = -1
                        self.cached_tracklist_hover = -1
                else:
                    self.hover_index = -1
                    self.cached_tracklist_hover = -1
                
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    if self.hover_index >= 0:
                        self.play_track(self.hover_index)
                    else:
                        for button_id in self.difficulty_buttons:
                            if self.is_in_radius(x, y, config.screen_width*.236 + button_id*60, self.difficulty_buttons_y, self.icon_r):
                                renpy.play("gui/sfx/select.ogg")
                                persistent.rhythm_difficulty = button_id
                                self.regenerate_scores()
                        
                        if self.is_in_radius(x, y, self.dark_mode_button_pos[0], self.dark_mode_button_pos[1], self.icon_r):
                            renpy.play("gui/sfx/select.ogg")
                            persistent.rhythm_dark = not persistent.rhythm_dark
                            self.request_redraw = True
                        
                        if x > self.exit_button_pos[0] and x < self.exit_button_pos[0]+self.icon_r*6 and y > self.exit_button_pos[1] and x < self.exit_button_pos[1]+self.icon_r:
                            renpy.play("gui/sfx/select.ogg")
                            self.request_exit = True
                    
                    renpy.redraw(self, 0)
                
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    renpy.redraw(self, 0)
                
                renpy.restart_interaction()
                pass

            def visit(self):
                return self.drawables

            def read_setlist_file(self, setlist_path):
                setlist_path_full = os.path.join(config.gamedir, setlist_path)

                with open(setlist_path_full, 'rt') as f:
                    text = f.read()

                setlist = [tuple(entry.strip('"') for entry in string.split(', ')) for string in text.split('\n') if string.strip() != '' and string.strip()[0] != '#']
                for index, set in enumerate(setlist):
                    if len(set) < 4:
                        raise Exception('Setlist was invalid! Each line should contain four or more strings separated by commas')

                    # The Chibi Names element
                    chibi_names = []
                    if len(set) >= 5:
                        for char in set[4]:
                            if char not in set[4]:
                                raise Exception('Setlist was invalid! Unknown character \'' + char + '\'\nValid characters are N, S, Y, M or a combination of these letters')
                            chibi_names.append(self.chibi_name_map[char])

                        modified_tuple = tuple(chibi_names if i == 4 else value for i, value in enumerate(set))
                        setlist[index] = modified_tuple
                    else:
                        setlist[index] = (*set[:4], chibi_names) # append empty chibi list
                return setlist

            def is_in_radius(self, x, y, x2, y2, r):
                distance = math.sqrt((x - x2-r) ** 2 + (y - y2-r) ** 2)
                return distance <= r

            def play_track(self, track_index):
                renpy.play("gui/sfx/select.ogg")
                self.request_song = self.setlist[track_index]

            def get_difficulty_text(self):
                return self.difficulties[persistent.rhythm_difficulty][0]
            
            def get_difficulty_color(self):
                return self.difficulties[persistent.rhythm_difficulty][1]

            def regenerate_scores(self):
                i = 0
                for text in self.sl_text:
                    title = text[1].text[0]
                    score = self.get_score(title)

                    # color in some of the stars
                    new_stars = self.get_recolored_stars(score)

                    # display highscores
                    regen = (
                        text[0], 
                        text[1], 
                        text[2], 
                        Text(self.get_formatted_score(title), xalign=1.0, yalign=0, size=16, font=DPRev.font_linkin()), 
                        new_stars
                        )
                    self.sl_text[i] = regen
                    i += 1

            def get_recolored_stars(self, score):
                new_stars = [Transform(Image(self.get_random_star_image())) for _ in range(3)]
                if score > 0:
                    new_stars[0] = DPRev.Shared.recolorize(self.get_random_star_image(), self.star_color, self.star_color)
                    if score >= DPRev.RhythmGame.get_max_score(persistent.rhythm_difficulty) * 0.9:
                        new_stars[1] = DPRev.Shared.recolorize(self.get_random_star_image(), self.star_color, self.star_color)
                        if score >= DPRev.RhythmGame.get_max_score(persistent.rhythm_difficulty):
                            new_stars[2] = DPRev.Shared.recolorize(self.get_random_star_image(), self.star_color, self.star_color)
                return new_stars

            def get_random_star_image(self):
                return renpy.random.choice(self.stars_images[:len(self.stars_images)])

            def get_formatted_score(self, title):
                return str(self.get_score(title))
            
            def get_score(self, title):
                if persistent.rhythm_highscores == None:
                    return 0

                data = persistent.rhythm_highscores[persistent.rhythm_difficulty]

                if data == None or title not in data:
                    return 0

                return int(data[title])

            def save_score(self, title, score, difficulty):

                # Generate data for the first time
                if persistent.rhythm_highscores == None:
                    persistent.rhythm_highscores = {
                        0: None, # EASY
                        1: None, # NORMAL
                        2: None, # HARD
                        3: None  # EXPERT
                    }

                data = persistent.rhythm_highscores[difficulty]
                if data == None:
                    data = { title: score }
                elif title not in data:
                    data.update({ title: score }) # add two dictionaries
                elif score > data[title]:
                    data[title] = score
                
                persistent.rhythm_highscores[difficulty] = data

            def delete_all_data(self):
                persistent.rhythm_highscores = None

        # Standalone game
        class RhythmGame(renpy.Displayable):

            DIFFICULTY_OPTIONS = {
                0: (5, 2, 0.25), # speed, skip_notes, score_mult
                1: (3, 2, 0.5),
                2: (3, 1, 1.0),
                3: (1.5, 1, 1.1) # third param should be either 1.0 or 1.1
            }
            SCORE_MAX = 1000000

            def __init__(self, audio_path, beatmap_path, difficulty, chibi_names):
                super(DPRev.RhythmGame, self).__init__()

                self.audio_path = audio_path

                self.has_started = False
                self.has_ended = False
                self.is_paused = False
                # the first st
                # an offset is necessary because there might be a delay between when the
                # displayable first appears on screen and the time the music starts playing
                # seconds, same unit as st, shown time
                self.time_offset = None
                self.time_paused = None

                # define some values for offsets, height and width
                # of each element on screen

                # offset from the left of the screen 
                self.x_offset = 700
                self.book_width = 280
                self.track_bar_height = int(config.screen_height * 0.84)
                self.track_bar_width = 12
                self.horizontal_bar_height = 8
                self.pause_bar_width = 600
                self.pause_bar_height = 100

                self.note_width = 50 # the actual arrow image is 50px, so this is 50
                self.note_outline_width = 64
                self.bark_time = .6
                self.fadeout_time = .4
                # soom in on the notw when it is hittable
                self.zoom_scale = 1.2
                self.zoom_time = 0.25 # 0 also looks good
                self.bark_zoom_scale = .8
                self.bark_width = 138*self.bark_zoom_scale # Should be actual width of image in pixels
                # offset the note to the right so it shows at the center of the track
                self.note_xoffset = (self.track_bar_width - self.note_width) / 2
                self.note_xoffset_large = (self.track_bar_width - self.note_width * self.zoom_scale) / 2

                self.miss_track = -1 # if there is a miss on a track

                self.input_allowed = True
                self.start_delay = 2

                # Since the notes are scroling from the screen top to bottom
                # they appear on the tracks prior to the onset time
                # this scroll time is also the note's entire lifespan time before it's eventually
                # hit or considered a miss
                # the note now takes 3 seconds to travel the screen
                # can be used to set difficulty level of the game
                self.note_offset = 3.0 

                # number of track bars
                self.num_track_bars = 4
                # drawing position
                self.track_bar_spacing = self.book_width / (self.num_track_bars - 1)
                # the xoffset of each track bar
                self.track_xoffsets = {
                    track_idx: self.x_offset + track_idx * self.track_bar_spacing
                    for track_idx in range(self.num_track_bars)
                }

                # define the notes' onset times

                self.onset_times = self.read_beatmap_file(beatmap_path)
                # can skip onsets to adjust difficulty level
                # skip every other onset so the display is less dense

                self.num_notes = len(self.onset_times)
                # assign notes to tracks, same length as self.onset_times
                self.random_track_indices = [
                    # upperbound inclusive generator (0-3)
                    renpy.random.randint(0, self.num_track_bars - 1) for _ in range(self.num_notes)
                ]

                self.difficulty = difficulty

                # did you just turn a rhythm game into a points-based poem game? yes... if 4 chibis are present...
                self.chibi_points = {
                    track_idx: 0 for track_idx in range(self.num_track_bars)
                }

                self.set_difficulty(self.difficulty)

                # speed is distance / time
                self.note_speed = config.screen_height / self.note_offset

                # maps track_idx to a list [] of active note timestamps
                # AKA: Is note on screen? (IS onset time within 3.0 seconds) or if it's still WAYYY off the screen
                # _______Concise way of creating a dictionary in PYTHON:__________________________________________
                # It assigns an empty list [] as the value for each track_idx key in the dictionary.
                # Think "ECMASCRIPT-5 Bullshit" we make up a variable track_idx and YES it has to be written twice
                # Literally makes this: {0: [], 1: [], 2: [], 3: [], 4: []}
                self.active_notes_per_track = {
                    track_idx: [] for track_idx in range(self.num_track_bars)
                }

                # barks stay active for a couple seconds before vanishing
                self.active_barks_per_track = {
                    track_idx: [] for track_idx in range(self.num_track_bars)
                }
                
                # when notes are hit, a fadeout effect is created and shown for almost a second
                self.active_fadeouts_per_track = {
                    track_idx: [] for track_idx in range(self.num_track_bars)
                }

                self.combo_bonus_max = 10
                self.score = 0
                self.combo = 0

                # detect and record hits
                # map onset timestamp to whether it has been hit, initialize
                self.onset_hits = {
                    onset: False for onset in self.onset_times
                }
                self.num_hits = 0
                self.num_possible_hits = 0 # increases as song increases
                self.latest_hit = 0 # used to calculate misses
                # if the note is hit within 0.3 seconds of it's actual onset
                # we consider it a hit
                # we can set different threshold for Good, Great hit scoring

                self.hit_thresholds = { # seconds
                    1: 0.3,
                    2: 0.2,
                    3: 0.1
                }

                self.score_bonuses = {
                    1: 1,
                    2: 2,
                    3: 5,
                }

                self.score_text_cached_time = 0
                self.score_default_text_size = 48
                self.score_text_size = 48
                self.score_text_color = '#fff'

                # map pygame key code to track idx
                self.keycode_to_track_idx = {
                    pygame.K_LEFT: 0,
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 2,
                    pygame.K_RIGHT: 3
                }

                # define the drawables
                self.pause_rect_drawable = Solid('#fff', xsize=self.pause_bar_width, ysize=self.pause_bar_height)
                self.pause_rect2_drawable = Solid('#000', xsize=self.pause_bar_width-20, ysize=self.pause_bar_height-20)
                self.pause_text = Text("( SPACE )", xalign=.5, yalign=.5, font=DPRev.font_linkin(), size=32)

                # map track_idx to the note drawable
                self.note_drawables = {
                    0: Image('mod_assets/rhythm/gui/a_left.png' if persistent.rhythm_dark == False else 'mod_assets/rhythm/gui/a_left_dark.png'),
                    1: Image('mod_assets/rhythm/gui/a_up.png' if persistent.rhythm_dark == False else 'mod_assets/rhythm/gui/a_up_dark.png'),
                    2: Image('mod_assets/rhythm/gui/a_down.png' if persistent.rhythm_dark == False else 'mod_assets/rhythm/gui/a_down_dark.png'),
                    3: Image('mod_assets/rhythm/gui/a_right.png' if persistent.rhythm_dark == False else 'mod_assets/rhythm/gui/a_right_dark.png')
                }

                # Renpy automatic transform will take input and scale it up X (1.2) times
                self.note_drawables_large = {
                    0: Transform(self.note_drawables[0], zoom=self.zoom_scale),
                    1: Transform(self.note_drawables[1], zoom=self.zoom_scale),
                    2: Transform(self.note_drawables[2], zoom=self.zoom_scale),
                    3: Transform(self.note_drawables[3], zoom=self.zoom_scale),
                }

                outline_path = 'mod_assets/rhythm/gui/a_outline.png' if persistent.rhythm_dark == False else 'mod_assets/rhythm/gui/a_outline_dark.png'
                self.note_drawables_outline = {
                    0: Transform(outline_path, rotate=270),
                    1: Transform(outline_path, rotate=0),
                    2: Transform(outline_path, rotate=180),
                    3: Transform(outline_path, rotate=90),
                }

                self.bark_drawables = {
                    0: Transform('mod_assets/rhythm/gui/w_miss.png', zoom=self.bark_zoom_scale),
                    1: Transform('mod_assets/rhythm/gui/w_bad.png', zoom=self.bark_zoom_scale),
                    2: Transform('mod_assets/rhythm/gui/w_good.png', zoom=self.bark_zoom_scale),
                    3: Transform('mod_assets/rhythm/gui/w_perfect.png', zoom=self.bark_zoom_scale)
                }

                self.possible_chibis_images = {
                    "Sayori": ( 'gui/poemgame/s_sticker_1.png', 'gui/poemgame/s_sticker_2.png' ),
                    "Natsuki": ( 'gui/poemgame/n_sticker_1.png', 'gui/poemgame/n_sticker_2.png' ),
                    "Yuri": ( 'gui/poemgame/y_sticker_1.png', 'gui/poemgame/y_sticker_2.png' ),
                    "Monika": ( 'gui/poemgame/m_sticker_1.png', 'gui/poemgame/m_sticker_2.png' )
                }

                # evently space out all chibis
                self.chibis = []
                if len(chibi_names) != 0:
                    stage_length = 200
                    c_offset_s = stage_length/len(chibi_names)
                    c_offset = -stage_length
                    for chibi_name in chibi_names:
                        c_offset += c_offset_s
                        chibi_image = self.possible_chibis_images[chibi_name]
                        self.chibis.append(DPRev.Shared.Chibi(chibi_image[0], chibi_image[1], x=350+c_offset, y=config.screen_height*.72))
                        c_offset += c_offset_s
                
                # record all drawables for self.visit [AKA: put them in a list]
                self.drawables = [
                    self.pause_rect_drawable,
                    self.pause_rect2_drawable,
                    self.pause_text
                ]
                # add these note drawables to self.drawables (which will be visited by self.visit)
                self.drawables.extend(list(self.note_drawables.values()))
                self.drawables.extend(list(self.note_drawables_large.values()))
                self.drawables.extend(list(self.note_drawables_outline.values()))
                self.drawables.extend(list(self.bark_drawables.values()))
            
            # Create renpy object with width & height parameters
            def render(self, width, height, st, at):
                """
                st: A float, the shown timebase, in seconds
                The shown timebase begins when this displayable is first shown on the screen
                """
                # Cache the first st, when this displayable is first shown on the screen
                # this allows us to compute subsequent times when the notes should appear

                # first time random num gen is called / first time displayable is shown
                if self.time_offset is None:
                    self.time_offset = st
                    renpy.music.stop(fadeout=0.5)
                    renpy.play("gui/sfx/select.ogg")
                    pygame.mouse.set_visible(False)

                # play music after delay
                if self.has_started == False and st - self.time_offset > self.start_delay:
                    # play music here
                    renpy.music.play(self.audio_path, loop=False)
                    self.has_started = True

                render = renpy.Render(width, height)

                # render the "winning" chibi on top (only applies when 4 are present)
                if len(self.chibis) != 0:
                    max_key = 0
                    max_points = float('-inf')
                    for key, value in self.chibi_points.items():
                        if value > max_points:
                            max_points = value
                            max_key = key
                    chibi_i = 0
                    for chibi in self.chibis:
                        if chibi_i != max_key:
                            chibi.render(render, st, at)
                        chibi_i += 1
                    self.chibis[max_key].render(render, st, at)

                # score text
                if self.score_text_size > self.score_default_text_size:
                    score_time_norm = (st-self.time_offset - self.score_text_cached_time) * 2
                    self.score_text_size = max(self.score_default_text_size, self.score_text_size - score_time_norm)

                # outline for notes (at bottom)
                for track_idx in range(self.num_track_bars):
                    x_offset = self.x_offset + track_idx * self.track_bar_spacing-self.note_outline_width/2 - (self.note_outline_width-self.note_width)/2
                    y_offset = self.track_bar_height-self.note_outline_width/2 + (self.note_outline_width-self.note_width)
                    render.place(self.note_drawables_outline[track_idx], x=x_offset, y=y_offset)

                # paused screen
                if self.is_paused:
                    render.place(self.pause_rect_drawable, x=config.screen_width/2-self.pause_bar_width/2, y=config.screen_height/2-self.pause_bar_height/2)
                    render.place(self.pause_rect2_drawable, x=config.screen_width/2-(self.pause_bar_width-20)/2, y=config.screen_height/2-(self.pause_bar_height-20)/2)
                    render.place(self.pause_text, x=0, y=0)

                # draw the notes 
                if not self.is_paused:
                    
                    # check if the song has ended
                    if self.has_started and renpy.music.get_playing() is None:
                        if self.has_ended == False:
                            if len(self.chibis) != 0 and self.score >= DPRev.RhythmGame.SCORE_MAX * DPRev.RhythmGame.DIFFICULTY_OPTIONS[self.difficulty][2]:
                                if len(self.chibis) == self.num_track_bars:
                                    max_key = 0
                                    max_points = float('-inf')
                                    for key, value in self.chibi_points.items():
                                        if value > max_points:
                                            max_points = value
                                            max_key = key
                                    self.chibis[max_key].jump(st, 10)
                                else:
                                    for chibi in self.chibis:
                                        chibi.jump(st, 10)
                            renpy.timeout(0) # raise an event immediately (0 is time to wait before raising event)
                        pygame.mouse.set_visible(True)
                        self.has_ended = True
                        renpy.redraw(self, 0)
                        return render

                    # the number of seconds the song has been playing
                    # is the difference between the current shown time (new st passed into render func) 
                    # and the cached first st
                    curr_time = st - self.time_offset

                    self.active_notes_per_track = self.get_active_notes_per_track(curr_time)

                    # render notes on each track
                    for track_idx in self.active_notes_per_track:
                        # look up track xoffset
                        x_offset = self.track_xoffsets[track_idx]

                        # loop through active notes
                        for onset, note_timestamp in self.active_notes_per_track[track_idx]:
                            # render the notes that are active and haven't been hit
                            if self.onset_hits[onset] is False:

                                note_drawable = self.note_drawables[track_idx]

                                # zoom in on the note if it is within the hit threshold
                                if abs(curr_time - onset) <= self.get_hit_threshold(1):
                                    if self.zoom_time != 0:
                                        elapsed_time = abs(curr_time-onset+self.get_hit_threshold(1))
                                        lerp = 1 + (self.zoom_scale-1) * (elapsed_time / self.zoom_time)
                                        lerp = min(lerp, self.zoom_scale)
                                        new_zoom_scale = lerp

                                        note_xoffset = x_offset + self.note_xoffset_large*lerp*(1/self.zoom_scale) # 1 is normal zoom
                                    else:
                                        new_zoom_scale = self.zoom_scale
                                        note_xoffset = x_offset + self.note_xoffset_large
                                else:
                                    new_zoom_scale = 1.0
                                    note_xoffset = x_offset + self.note_xoffset
                                
                                # compute where on the vertical axes the note is
                                # the vertical distance from the top that the note has already traveled
                                # is given by time * speed
                                note_distance_from_top = note_timestamp * self.note_speed
                                y_offset = self.track_bar_height - note_distance_from_top
                                new_note_drawable = Transform(note_drawable, zoom=new_zoom_scale)
                                render.place(new_note_drawable, x=note_xoffset, y=y_offset)
                            else:
                                # we will show the hit text later
                                continue

                    # render note fadeout effects
                    removed_objects = []
                    for track_idx in self.active_fadeouts_per_track:
                        x_offset = self.track_xoffsets[track_idx]
                        for y_offset, c_time in self.active_fadeouts_per_track[track_idx]:

                            elapsed_time = abs(curr_time-c_time)
                            new_zoom_scale = self.zoom_scale*((elapsed_time / self.fadeout_time) ** .3)*0.5

                            # Use 'Zoomed in' version of note ONLY
                            note_drawable = self.note_drawables_large[track_idx]
                            note_xoffset = x_offset + self.note_xoffset_large
                            note_xoffset = x_offset + ((self.track_bar_width - (self.note_width*self.zoom_scale + self.note_width*self.zoom_scale*new_zoom_scale)) / 2)
                            
                            alpha_mult = .1 if persistent.rhythm_dark else 2
                            alpha_value = 1 - ((elapsed_time / self.fadeout_time) ** alpha_mult)
                            glow_sat_alpha = (1 + (elapsed_time / self.fadeout_time) ** .3) * 5
                            glow_bri_alpha = (elapsed_time / self.fadeout_time) ** .3

                            fadeout_drawable = Image(self.note_drawables[track_idx])
                            glow_effect = Transform(fadeout_drawable)
                            glow_effect.matrixcolor = BrightnessMatrix(glow_bri_alpha*.3) * SaturationMatrix(glow_sat_alpha*.3)
                            glow_effect = Transform(glow_effect, zoom=self.zoom_scale + new_zoom_scale)
                            glow_effect.alpha = alpha_value
                            render.place(glow_effect, x=note_xoffset, y=y_offset)
                            pass

                        self.active_fadeouts_per_track[track_idx] = [tup for tup in self.active_fadeouts_per_track[track_idx] if curr_time-tup[1] < self.fadeout_time]

                    # Cleanup the removed objects
                    for obj in removed_objects:
                        # Delete or release any associated resources
                        del obj  # Or obj.cleanup() or obj.release_resources() depending on the object type

                    # handle misses found in get_active_notes_per...
                    if self.miss_track != -1:

                        # Lower score if they just started (get negative points, lol)
                        if self.score <= 0:
                            self.score -= 200
                        elif self.score <= 10000:
                            self.score -= 500
                        
                        self.combo = 0

                        # append bark ID (miss is 0), y_position (in this case just use bottom of screen), current time
                        self.active_barks_per_track[self.miss_track].append((0, self.track_bar_height-renpy.random.randint(0, 20)+70, curr_time))
                        self.miss_track = -1

                    for track_idx in self.active_barks_per_track:
                        x_offset = self.x_offset + track_idx * self.track_bar_spacing-self.bark_width/2
                        for bark_id, y_position, c_time in self.active_barks_per_track[track_idx]:

                            # 1. Move up (and slow down)
                            elapsed_time = abs(curr_time-c_time)
                            
                            # 2. fade
                            alpha_value = 1 - ((elapsed_time / self.bark_time) ** 3.5)
                            bark_drawable = Transform(self.bark_drawables[bark_id])
                            bark_drawable.alpha = alpha_value

                            render.place(bark_drawable, x=x_offset, y=y_position+elapsed_time*20)

                        self.active_barks_per_track[track_idx] = [tup for tup in self.active_barks_per_track[track_idx] if curr_time-tup[2] < self.bark_time]

                # 0 means renpy will redraw displayable after 0 seconds. AKA: Immediately
                renpy.redraw(self, 0)
                return render

            def event(self, ev, x, y, st):
                
                # if music has ended
                if self.has_ended:
                    # refresh the screen
                    renpy.restart_interaction()
                    return
                # check if some keys have have pressed
                if ev.type == pygame.KEYDOWN:

                    # pause game
                    if ev.key == pygame.K_ESCAPE:
                        if self.is_paused == False:
                            # ON PAUSE
                            pygame.mouse.set_visible(True)
                            curr_time = st - self.time_offset
                            self.time_paused = curr_time
                            renpy.music.set_pause(True)
                        self.is_paused = True
                    if ev.key == pygame.K_SPACE:
                        renpy.play("gui/sfx/select.ogg")
                        self.is_paused = not self.is_paused
                        if self.is_paused:
                            # ON PAUSE
                            pygame.mouse.set_visible(True)
                            curr_time = st - self.time_offset
                            self.time_paused = curr_time
                            renpy.music.set_pause(True)
                        else:
                            # ON RESUME
                            pygame.mouse.set_visible(False)
                            self.time_offset = st - self.time_paused
                            renpy.music.set_pause(False)
                        return
                    if self.is_paused:
                        return

                    # only handle the four keys we defined -- and only allow one note hit at once
                    if not ev.key in self.keycode_to_track_idx or self.input_allowed == False:
                        return
                    # look up the track that corresponds to the key pressed
                    track_idx = self.keycode_to_track_idx[ev.key]

                    active_notes_on_track = self.active_notes_per_track[track_idx]
                    curr_time = st - self.time_offset # st - (our cached first shown timebase)

                    # loop over active notes to check if one is hit
                    for onset, note_timestamp in active_notes_on_track:
                        # compute the time difference between when the key is pressed
                        # and when we consider the note hittable as defined by hit threshold (0.3)
                        # dif of cur time and onset time is smaller than threshold
                        if abs(curr_time - onset) <= self.get_hit_threshold(1) and self.onset_hits[onset] is False:
                            self.onset_hits[onset] = True
                            self.num_hits += 1
                            self.combo += 1
                            self.latest_hit = self.num_possible_hits

                            # create an effect
                            note_distance_from_top = note_timestamp * self.note_speed
                            y_offset = self.track_bar_height - note_distance_from_top

                            # Remove expired fadeouts
                            self.active_fadeouts_per_track[track_idx].append((y_offset, curr_time))

                            # Add new fadeout
                            self.active_fadeouts_per_track[track_idx].append((y_offset, curr_time))

                            # # Remove expired fadeouts
                            # if self.active_fadeouts_per_track[track_idx]:
                            #     while self.active_fadeouts_per_track[track_idx] and self.active_fadeouts_per_track[track_idx][0][1] < curr_time:
                            #         self.active_fadeouts_per_track[track_idx] = self.active_fadeouts_per_track[track_idx][1:]

                            # # Add new fadeout
                            # self.active_fadeouts_per_track[track_idx].append((y_offset, curr_time))


                            for bark_id in reversed(self.hit_thresholds):
                                if abs(curr_time - onset) <= self.get_hit_threshold(bark_id):
                                    self.active_barks_per_track[track_idx].append((bark_id, self.track_bar_height-renpy.random.randint(5, 25)+50, curr_time))

                                    # Chibi jumps if PERFECT note is hit
                                    if len(self.chibis) != 0 and bark_id >= 3 and renpy.random.random() < .1:
                                        if len(self.chibis) == self.num_track_bars:
                                            self.chibis[track_idx].jump(st)
                                            self.chibi_points[track_idx] += 1
                                        else:
                                            self.chibis[renpy.random.randint(0, len(self.chibis)-1)].jump(st)

                                    # Score Text FX
                                    if bark_id >= 2:
                                        if self.score > DPRev.RhythmGame.SCORE_MAX*DPRev.RhythmGame.DIFFICULTY_OPTIONS[1][2]: # NORMAL
                                            text_size_increase = 6
                                        else:
                                            text_size_increase = 3
                                        self.score_text_size = self.score_default_text_size+text_size_increase
                                        self.score_text_cached_time = curr_time

                                    # Score Related
                                    difficulty_option = DPRev.RhythmGame.DIFFICULTY_OPTIONS[self.difficulty]
                                    account_for_combo_buildup = 0

                                    for combo_value in range(1, self.combo_bonus_max + 1):
                                        # Calculate the potential note score for this combo value
                                        num_notes = self.num_notes/difficulty_option[1] # normally difficulty_option[1] means 1. If this is 2 it means it skips every other note
                                        note_score = (DPRev.RhythmGame.SCORE_MAX * self.score_bonuses[3]) / (num_notes * self.score_bonuses[bark_id])
                                        # Increment the account_for_combo_buildup based on potential note score
                                        account_for_combo_buildup += (note_score * min(combo_value, self.combo_bonus_max)) / self.combo_bonus_max
                                    
                                    note_score = ((DPRev.RhythmGame.SCORE_MAX + account_for_combo_buildup) * self.score_bonuses[bark_id]) / (num_notes * self.score_bonuses[3])
                                    note_score = (note_score * min(self.combo, self.combo_bonus_max)) / self.combo_bonus_max
                                    # [1] determines if there are less notes (score must be multipled), [2] is overall score mult
                                    self.score += note_score * difficulty_option[2]
                                    self.score = min(DPRev.RhythmGame.SCORE_MAX*difficulty_option[2], self.score)

                                    # Hitting a BAD note resets the combo
                                    if bark_id <= 1:
                                        self.combo = 0
                                    break
                                
                            # Score Text FX
                            if self.score >= DPRev.RhythmGame.SCORE_MAX:
                                self.score_text_color = '#FFD800'
                            elif self.score >= DPRev.RhythmGame.SCORE_MAX*DPRev.RhythmGame.DIFFICULTY_OPTIONS[1][2]: # NORMAL
                                self.score_text_color = '#7FFFFF'
                            elif self.score >= DPRev.RhythmGame.SCORE_MAX*DPRev.RhythmGame.DIFFICULTY_OPTIONS[0][2]: # EASY
                                self.score_text_color = '#B200FF'
                            
                            # redraw immediately because now the note should disappear
                            renpy.redraw(self, 0) # redraw after delay of 0
                            # refresh the screen
                            renpy.restart_interaction()
                            break
                    self.input_allowed = False
                else:
                    if ev.type == pygame.KEYUP:
                        if not ev.key in self.keycode_to_track_idx:
                            return
                        self.input_allowed = True

                    renpy.restart_interaction()

            def visit(self):
                return self.drawables # return drawables list we made in init

            def get_active_notes_per_track(self, current_time):
                active_notes = {
                    track_idx: [] for track_idx in range(self.num_track_bars)
                }
                self.num_possible_hits = 0

                # it just so happens self.onset_times and self.random_track_indices have the same length, so...
                # we can loop over them simultaneously using python's zip function
                for onset, track_idx in zip(self.onset_times, self.random_track_indices):
                    # determine if this note should appear on the track
                    time_before_appearance = onset - current_time

                    # should we declare the note as active
                    if time_before_appearance < -.5: # already below the bottom of the screen (0 is perfect)
                        if self.num_possible_hits > self.latest_hit and self.onset_hits[onset] is False:
                            self.miss_track = track_idx
                            self.latest_hit = self.num_possible_hits
                        self.num_possible_hits += 1
                        continue
                    # should be on screen
                    # recall that self.note_offset is 3 seconds, the note's lifespan
                    elif time_before_appearance <= self.note_offset:
                        # append tuple consisting of onset time and time before appearance to track the notes correspond to
                        active_notes[track_idx].append((onset, time_before_appearance))
                    # there is still time before the next note should show
                    # break out of the loop so we don't process subsequent notes that are even later into the music
                    elif time_before_appearance > self.note_offset:
                        break
                return active_notes

            def read_beatmap_file(self, beatmap_path):
                # read newline separated floats
                beatmap_path_full = os.path.join(config.gamedir, beatmap_path)

                # opens specified file in text mode ('rt')
                with open(beatmap_path_full, 'rt') as f:
                    # reads entire contact of file 'f' and stores it in string 'text'
                    text = f.read()

                # splits text into multiple substrings using \n as delimeter
                # [float(string) for string in ...] iterates over each line
                # float(string) converts non-empty line to a floating-point number and adds it to the onset_times list
                #onset_times = [float(string) for string in text.split('\n') if string != '']
                onset_times = [float(string)+self.start_delay for string in text.split('\n') if string != '']
                # for i in range(len(onset_times)):
                #     onset_times[i] += self.start_delay

                return onset_times

            def get_hit_threshold(self, id):
                # hit_threshold multiplier 1 = note offset (4,3,1.5) / hard mode note offset (3)
                speed_mod = DPRev.RhythmGame.DIFFICULTY_OPTIONS[self.difficulty][0] / DPRev.RhythmGame.DIFFICULTY_OPTIONS[2][0]
                if self.difficulty >= 3: # make it slightly easier
                    speed_mod *= 1.5
                return self.hit_thresholds[id] * speed_mod

            def set_difficulty(self, difficulty):
                option = DPRev.RhythmGame.DIFFICULTY_OPTIONS[difficulty]

                # slow down/speed up notes
                self.note_offset = option[0]

                # skip notes
                if option[1] > 1:
                    self.onset_times = self.onset_times[::2]

            def get_formatted_score(self):
                return "{:,}".format(int(self.score))

            def get_formatted_score_k(self):
                score = int(self.score)
                expertMult = DPRev.RhythmGame.DIFFICULTY_OPTIONS[3][2]
                if score > DPRev.RhythmGame.SCORE_MAX*expertMult and expertMult > 1.0:
                    formatted_str = "{:.1f} Million".format(DPRev.floor(score / 100000) * 0.1)
                elif score >= DPRev.RhythmGame.SCORE_MAX:
                    formatted_str = "1 Million"
                elif score >= 100000:
                    formatted_str = "{:.0f}K".format(DPRev.floor(score / 50000) * 50)
                elif score >= 10000:
                    formatted_str = "{:.0f}K".format(DPRev.floor(score / 10000) * 10)
                else:
                    formatted_str = str(DPRev.floor(score / 1000) * 1000)
                return formatted_str

            @staticmethod
            def get_max_score(difficulty):
                return DPRev.RhythmGame.SCORE_MAX * DPRev.RhythmGame.DIFFICULTY_OPTIONS[difficulty][2]