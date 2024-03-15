# Interactive Map (Pan not supported) - By Rimscar
# Feel free to use/edit/modify in your projects. Credit is nice, but not required. Just keep this disclaimer.
#
# Actual code starts below the 'label' section 
# NOTE: Kept the labels here as they are good examples of how to implement the map.

image bg_map cipher = "mod_assets/map/bg.jpg"

label ch2_map:
    play music s3
    window hide
    scene bg_map cipher

    $ activities = ["CHURCH"]
    if persistent.arcade_unlocked:
        $ activities.append("ARCADE")
    $ activities.extend(["SHOPPING", "DATE", "GREENHOUSE"])
    
    call screen map_select(activities, time="5:05 PM")
    $ activity = _return
    $ quick_menu = True
    scene black
    stop music fadeout 1.0

    if activity == "CHURCH":
        call jesus from _call_jesus
    elif activity == "ARCADE":
        call arcade from _call_arcade
    elif activity == "SHOPPING":
        call ch2_a1 from _call_ch2_a1
    elif activity == "DATE":
        call ch2_a2 from _call_ch2_a2
        $ act_monika_date = True
    elif activity == "GREENHOUSE":
        call ch2_a3 from _call_ch2_a3
        $ act_greenhouse = True
    return

label ch3_map:
    play music s3
    window hide
    scene bg_map cipher

    $ activities = ["PAWNSHOP1"]
    if persistent.arcade_unlocked:
        $ activities.append("ARCADE")
    $ activities.append("TAKEOUT")
    $ activities.append("SHRINE")
    if act_greenhouse == False:
        $ activities.append("GREENHOUSE")
    
    call screen map_select(activities, time="5:10 PM")
    $ activity = _return
    $ quick_menu = True
    scene black
    stop music fadeout 1.0
    
    if activity == "PAWNSHOP1":
        call ch3_a1 from _call_ch3_a1
        $ act_pawnshop1 = True
    elif activity == "ARCADE":
        call arcade from _call_arcade_1
    elif activity == "TAKEOUT":
        call ch3_a2 from _call_ch3_a2
        $ act_met_kaito = True
    elif activity == "SHRINE":
        call ch3_a3 from _call_ch3_a3
        $ act_visit_shrine = True
    elif activity == "GREENHOUSE":
        call ch2_a3 from _call_ch2_a3_1
        $ act_greenhouse = True
    return

label ch4_map:
    window hide

    $ activities = ["SAYORI_ARCADE"]
    if act_pawnshop1 == False:
        $ activities.append("PAWNSHOP1")
    else:
        $ activities.append("PAWNSHOP2")
    if act_greenhouse:
        $ activities.append("MUSEUM")
    if act_met_kaito:
        $ activities.append("TOWER")
    
    call screen map_select(
        activities, 
        time="3:41 PM", 
        overcast=True, 
        fade_to_black=False,
        initial_activity=InteractiveMap.DummyActivity(-2600, -1080, 580, 360, "Suburbs"))
    $ activity = _return
    $ quick_menu = True

    if activity == "SAYORI_ARCADE":
        call ch4_a1 from _call_ch4_a1
        $ persistent.arcade_unlocked = True
    elif activity == "PAWNSHOP1":
        call ch3_a1 from _call_ch3_a1_1
        $ act_pawnshop1 = True
    elif activity == "PAWNSHOP2":
        call ch4_a2 from _call_ch4_a2
        $ act_pawnshop2 = True
    elif activity == "MUSEUM":
        call ch4_a3 from _call_ch4_a3
        $ act_museum = True
    elif activity == "TOWER":
        call ch4_a4 from _call_ch4_a4
        $ act_kaito_job = True
    return

label ch5_map:
    play music s3
    window hide
    scene bg_map cipher

    $ activities = []
    if act_pawnshop1 == False:
        $ activities.append("PAWNSHOP1")
    elif act_pawnshop2 == False:
        $ activities.append("PAWNSHOP2")
    elif act_pawnshop2:
        $ activities.append("PAWNSHOP3")
    $ activities.extend(["ARCADE", "GACHAPON", "RAMEN1"])
    if act_museum:
        $ activities.append("ROOF")
    
    call screen map_select(activities, time="5:03 PM")
    $ activity = _return
    $ quick_menu = True
    scene black
    stop music fadeout 1.0

    if activity == "PAWNSHOP1":
        call ch3_a1 from _call_ch3_a1_2
        $ act_pawnshop1 = True
    elif activity == "PAWNSHOP2":
        call ch4_a2 from _call_ch4_a2_1
        $ act_pawnshop2 = True
    elif activity == "PAWNSHOP3":
        call ch5_a1 from _call_ch5_a1
        $ persistent.key = True
    elif activity == "ARCADE":
        $ persistent.arcade_unlocked = True
        call arcade from _call_arcade_2
    elif activity == "GACHAPON":
        call ch5_a2 from _call_ch5_a2
        $ act_gachapon = True
    elif activity == "RAMEN1":
        call ch5_a3 from _call_ch5_a3
        $ act_ramen1 = True
    elif activity == "ROOF":
        call ch5_a4 from _call_ch5_a4
        $ act_akemi_roof = True
    return

label ch5_fair_map:
    play music s3
    window hide
    scene bg_map cipher

    $ activities = ["FAIR"]

    if act_akemi_roof:
        $ dummy_activity = InteractiveMap.DummyActivity(-2400, -750, 600, 300, "Okayama High") # from roof/school
    elif act_ramen1:
        $ dummy_activity = InteractiveMap.DummyActivity(-2600, -1280, 730, 330, "Downtown") # Ramen
    else:
        $ dummy_activity = InteractiveMap.DummyActivity(-3300, -720, 880, 310, "Downtown") # Gachapon
    
    call screen map_select(activities, time="6:30 PM", initial_activity=dummy_activity)
    $ activity = _return
    $ quick_menu = True
    scene black
    stop music fadeout 1.0

    return

label interlude_map:
    window hide
    scene bg_map cipher
    play music amb_rain
    play sound "mod_assets/sfx/thunder.ogg"

    $ activities = ["RAMEN2"]
    if persistent.key:
        $ activities.append("LOCKER57")
    
    call screen map_select(
        activities, 
        time="9:00 AM", 
        overcast=True,
        initial_activity=InteractiveMap.DummyActivity(-2600, -1280, 500, 390, "Suburbs"))
    $ activity = _return
    $ quick_menu = True
    scene black

    if activity == "RAMEN2":
        call interlude_a1 from _call_interlude_a1
    elif activity == "LOCKER57":
        call interlude_a2 from _call_interlude_a2
        $ act_locker57 = True
    return

label ch7_map:
    play music s3
    window hide
    scene bg_map cipher

    $ activities = ["MOUNTAINS"]
    
    call screen map_select(
        activities, 
        map_speed=4.0, 
        time="10:00 PM",
        initial_activity=InteractiveMap.DummyActivity(-2575, -1425, 900, 480, "Kawasaki Residence"))
    $ activity = _return
    $ quick_menu = True
    scene black
    stop music fadeout 0.5
    pause 0.5
    play music amb_night

    return

# Give a list of activity_IDs (must match IDs in InteractiveMap.activity_tuples)
# Looks nice if given a list of 2-5 activities
screen map_select(activity_IDs, initial_activity=None, map_speed=1.5, time="", fade_to_black=True, overcast=False):
    default imap = InteractiveMap(
        activity_IDs, 
        initial_activity=initial_activity, 
        map_speed=map_speed, 
        time=time, 
        fade_to_black=fade_to_black, 
        overcast=overcast)
    add imap

    if imap.activity_ID != None:
        timer 0.001 action Return(imap.activity_ID)

init python:
    class InteractiveMap(renpy.Displayable):

        # ID, x, y, beacon_x, beacon_y, Character=None, bar_variation=None/B/C, Activity_Name, Location_name, Description_Top, Description_Bottom, (OPTIONAL) Password=1234
        activity_tuples = {

            # CHAPTER 2
            ("CHURCH", -2250, -1100, 700, 340, 'l', 'c', "Derelict Chapel", "Suburbs", "{font=mod_assets/map/font/ydady-code.otf}And what of agent Kuzuhara?\nAnother unfortunate accident, a necessary\nsacrifice in the line of duty, a man we mourn...\nAnd what of the shuutai?\nBurned, vaporized.\nKuzuhara saw to it personally, his last act of duty.", "{font=mod_assets/map/font/ydady-code.otf}what is it?\nIt says here... kuzuhara had a kid, a boy.\n\n{/font}Unable to Transcribe Message", "2Z7X"),
            ("ARCADE", -3300, -720, 1090, 220, None, None, "Arcade", "Downtown Okayama", "The Okayama Arcade is closed off from the streets and sky by steel netting, all the better to direct airflow away from the pedestrian street that runs below the shops.\n{i}{u}I need a break.", ""),
            ("SHOPPING", -3300, -720, 480, 450, 'n', None, "Shopping With Natsuki", "Downtown Okayama", "LOCALE:\n> Downtown Okayama\n\nARRIVAL:\n> Unexpected\n\nChances of This\nGoing Well: 0.0%", "I heard Natsuki will be shopping in downtown Okayama today, maybe I could tag along?"),
            ("DATE", -2590, -1200, 700, 300, 'm', None, "Ask Monika Out", "Suburbs", "> Kawasaki, Monika\n> EYE COLOR: GREEN\n\nADDRESS:\n> UNDETERMINED\n\nOCCUPATION:\n> S. C. President", "I'd like to continue our conversation from the drive over. She'll probably turn me down, but there's no harm in asking, right?"),
            ("GREENHOUSE", -1740, -750, 640, 400, 'g', None, "Water the Plants", "Okayama High", "", "Akemi, the girl I bumped into today, asked if I could water the plants in the old greenhouse. I think I remember the route from years back. On a warm day, I ended up getting caught in the nostalgia."),

            # CHAPTER 3
            ("PAWNSHOP1", -3300, -720, 750, 240, 'd', None, "Pawnshop", "Downtown Okayama", "", ""),
            ("TAKEOUT", -2750, -950, 620, 370, 'u', None, "Order Takeout", "Suburbs", "Ichiiwa Restaurant\n\nACTOR:\n> UNKNOWN\n\nOdds of a Chance Encounter: {i}HIGH", "There's this local takeout place, it's more of a store-front really, with just a few stools. When you say Tonkatsu, most people think Kishuya or some famous restaurant. But according to Sayori—"),
            ("SHRINE", -1940, -1080, 560, 400, None, None, "Visit the Shrine", "Green Shower Forest", "The shrine doesn't see many visitors these days, and this morning when I came for my customary visit, it was more deserted than usual.", ""),
            
            # CHAPTER 4
            ("PAWNSHOP2", -3300, -720, 750, 240, None, None, "Pawnshop", "Downtown Okayama", "The pawnshop in Hayashima is full of bric-a-brac: furniture from who knows when, chipped statuettes, old vinyl. It's hard for a passerby not to think 'junk,' but I don't even feel that—I just stop in on impulse.", ""),
            ("MUSEUM", -3800, -720, 1040, 300, 'v', 'c', "Museum", "Downtown Okayama", "", "The Museum of Evolution draws tourists by the busloads all throughout the year, except maybe over the holidays. Perhaps I should see what all of the hype is about?"),
            ("TOWER", -3800, -1426, 1070, 470, 'k', 'c', "Kaito's Job", "Coastline", "> ?????, Kaito\n> EYE COLOR: GREEN\n\nADDRESS:\n> UNDETERMINED\n\nOCCUPATION:\n> UNEMPLOYED", "Kaito has a photo of me and Yuri from the night of the accident, if I'm going to get to the bottom of this mess, going along with Kaito's request seems the only option."),
            ("SAYORI_ARCADE", -3300, -720, 1090, 220, 's', None, "Arcade With Sayori", "Downtown Okayama", "\"Say, would you, maybe... want to accompany me to the arcade?\"\n\nUNLOCKS:\n> THE ARCADE", "Sayori asked me to accompany her, nothing formal just two friends messing around. I don't really feel like playing games, but she's trying her best to cheer me up so I might as well go."),

            # CHAPTER 5
            ("PAWNSHOP3", -3300, -720, 750, 240, 'e', 'c', "Pawnshop", "Downtown Okayama", "{i}\"Yo, my guy.\"\n\n\"You're going to wanna hear this!\"\n\n- Eiji", "Eiji asked me to stop by the pawnshop on my way home. He seemed really excited earlier on the phone... said it would take a while so I should just come in person."),
            ("GACHAPON", -3300, -720, 880, 310, 'u', None, "Gachapon", "Downtown Okayama", "Downtown Gachapon\n\nACTOR:\n> UNKNOWN\n\nOdds of a Chance Encounter: {i}HIGH", "The downtown Gachapon beckons from the end of a small side street. In every color you can imagine, they have fluffy animals, tools and weapons, people, buildings, robots, cards and more!"),
            ("RAMEN1", -3300, -720, 730, 330, None, None, "Ramen Saburo", "Downtown Okayama", "The local Ramen Saburo, a hole in the wall restaurant hidden along a nondescript street, is considered by those in-the-know to make one of the best kamaage-don in Okayama.", ""),
            ("ROOF", -2400, -750, 756, 184, 'a', 'c', "Meet With Akemi", "Okayama High", "{i}\"We need to talk, in person. It's urgent.\"\n\n- Akemi", "I'm supposed to meet Akemi on the roof, though I'm not sure if I should really trust this girl...\n\nShe hasn't been totally upfront with me about her motives."),

            # CHAPTER 5 - Carnival
            ("FAIR", -3450, -1426, 520, 470, 'f', 'b', "Theme Park", "Coastline", "EXPECTING:\n> Monika\n> Sayori\n> Natsuki\n> Yuri\n{i}> ?????{/i}\n\n{font=mod_assets/map/font/ydady-code.otf}just three more minutes", "I don't know whose idea of a relaxing evening standing around watching everyone else hurl themselves off a mountain is, but Sayori was the one in charge of this activity, not me."),

            # INTERLUDE
            ("RAMEN2", -3300, -720, 730, 330, None, None, "Ramen Saburo", "Downtown Okayama", "Aside from ramen, the local saburo features lesser known dishes popular among the locals—namely Zosui, a rice soup seasoned only with soy sauce.", ""),
            ("LOCKER57", -3815, -1120, 1000, 380, 'w', 'c', "Locker 57", "Coastline", "RED DRAGON\nLOGISTICS\n\n> FORMER AIRFIELD\n> EX-MILITARY\n> LOCKER 57\n\n{font=mod_assets/map/font/ydady-code.otf}Koshien Naval Base off site storage", "An abandoned airfield converted into storage, Tamano Airstrip is surrounded by low, rolling hills.\n\nAside from the occasional blue security van, the site is deserted."),

            # CHAPTER 7
            ("MOUNTAINS", -15, -15, 590, 185, 't', None, "School Trip", "Mt. Atagoyama", "", "The clubs are taking a school trip to the mountains. The clean air should be a nice change of scenery, though I'm still worried about Yuri.\n\n{i}Hopefully my fears are unwarranted."),
        }

        def __init__(self, activity_IDs, initial_activity=None, map_speed=1.5, time="", fade_to_black=True, overcast=False):
            super(InteractiveMap, self).__init__()

            # Configuration
            self.activity_default = self.DummyActivity(-2400, -750, 600, 300, "Okayama High") if initial_activity == None else initial_activity

            # Don't touch
            self.activity_ID = None
            self.activity_list = self.get_activity_list(activity_IDs)
            self.x_current = self.activity_default.x
            self.y_current = self.activity_default.y
            self.x_cached = self.activity_default.x
            self.y_cached = self.activity_default.y
            self.lerp_start_time = -999
            self.lerp_duration = map_speed
            self.fade_time = 0
            self.fade_duration = 1.5
            self.hover_index = 0
            self.selected_index = -1
            self.hovering_embark = False
            self.is_fading_out = False
            self.fade_to_black = fade_to_black

            self.beacon = InteractiveMap.Beacon(0, 0)

            self.num_activities = len(activity_IDs)
            self.map_drawable = Image("mod_assets/map/map.jpg")
            self.bg_overlay = Image("mod_assets/map/bg_overlay.png")
            self.sidebar_drawable = Image("mod_assets/map/sidebar.png")
            self.sidebar_top_drawable = Image("mod_assets/map/top.png")
            self.icon_wireless = Image("mod_assets/map/icon_wireless.png")
            self.icon_location = Transform("mod_assets/map/icon_location.png", zoom=.2)
            self.icon_bluetooth = Transform("mod_assets/map/icon_bt.png", zoom=.3)
            self.icon_battery = Transform("mod_assets/map/icon_battery.png", zoom=.3)
            self.top_text = Text("3G Doki-DIRECT  /  " + ("5:00 PM" if time=="" else time) + "  /  Tuesday", xalign=0, yalign=0, font=self.get_font(), size=12)

            self.bar_variations = {
                'b': Image('mod_assets/map/barB.png'),
                'c': Image('mod_assets/map/barC.png')
            }
            self.bar_highlight_variations = {
                'b': Image('mod_assets/map/barB_h.png'),
                'c': Image('mod_assets/map/barC_h.png')
            }
            self.bars = {}
            for act_idx in range(self.num_activities):
                variation = self.activity_list[act_idx].bar_variation
                bar_img = Image("mod_assets/map/bar.png")
                bar_h_img = Image("mod_assets/map/bar_h.png")
                if variation != None:
                    bar_img = self.bar_variations[variation]
                    bar_h_img = self.bar_highlight_variations[variation]
                self.bars.update( { act_idx: (bar_img, bar_h_img)} )
            
            self.arrow = Transform("mod_assets/map/arrow.png",zoom=.5)
            self.desc_box = Image("mod_assets/map/desc_box.png")
            self.desc_box_highlight = Image("mod_assets/map/desc_box_h.png")
            self.desc_box_s = Image("mod_assets/map/desc_box_s.png")
            self.desc_box_s_highlight = Image("mod_assets/map/desc_box_s_h.png")
            self.bar_height = 29
            self.btn_embark = Image('mod_assets/map/btn_embark.png')
            self.btn_embark_h = Image('mod_assets/map/btn_embark_h.png')
            self.btn_embark_d = Image('mod_assets/map/btn_embark_disabled.png')
            self.btn_locked = Image('mod_assets/map/btn_locked.png')
            self.btn_locked_h = Image('mod_assets/map/btn_locked_h.png')

            self.portrait_back = Image('mod_assets/map/portrait.png')
            self.portraits = {
                'a': Transform('mod_assets/map/portraits/a.png',zoom=.227),
                'e': Transform('mod_assets/map/portraits/e.png',zoom=.227),
                'k': Transform('mod_assets/map/portraits/k.png',zoom=.227),
                'm': Transform('mod_assets/map/portraits/m.png',zoom=.227),
                'n': Transform('mod_assets/map/portraits/n.png',zoom=.227),
                's': Transform('mod_assets/map/portraits/s.png',zoom=.227),
                'u': Transform('mod_assets/map/portraits/unknown.png',zoom=.227),
                'l': Transform('mod_assets/map/portraits/logo.png',zoom=.227),
                'f': Transform('mod_assets/map/portraits/fair.png',zoom=.227),
                'w': Transform('mod_assets/map/portraits/warehouses.png',zoom=.227),
            }
            self.landscape_back = Image('mod_assets/map/landscape.png')
            self.landscapes = {
                'g': Transform('mod_assets/map/portraits/greenhouse.png',zoom=.227),
                'd': Transform('mod_assets/map/portraits/discount.png',zoom=.227),
                'v': Transform('mod_assets/map/portraits/museum.png',zoom=.227),
                't': Transform('mod_assets/map/portraits/shrine.png',zoom=.227),
            }
            self.bars_text = {
                act_idx: Text("?????", xalign=0, yalign=0, font=self.get_font(), size=13) for act_idx in range(self.num_activities)
            }
            self.bars_points = {
                act_idx: Solid('#fff', xsize=5, ysize=5) for act_idx in range(self.num_activities)
            }

            index = 0
            for activity in self.activity_list:
                for activity_tuple in InteractiveMap.activity_tuples:
                    if activity_tuple[0] == activity.ID:
                        self.bars_text[index].text = activity.activity_name
                index += 1

            self.drawables = [
                self.map_drawable,
                self.bg_overlay,
                self.sidebar_top_drawable,
                self.sidebar_drawable,
                self.icon_wireless,
                self.icon_location,
                self.icon_bluetooth,
                self.icon_battery,
                self.top_text,
                self.arrow,
                self.desc_box,
                self.desc_box_highlight,
                self.desc_box_s,
                self.desc_box_s_highlight,
                self.btn_embark,
                self.btn_embark_d,
                self.btn_embark_h,
                self.btn_locked,
                self.btn_locked_h,
                self.portrait_back,
                self.landscape_back,
            ]
            self.drawables.extend(list(self.bar_variations.values()))
            self.drawables.extend(list(self.bar_highlight_variations.values()))
            self.drawables.extend(list(self.bars_text.values()))
            self.drawables.extend(list(self.bars_points.values()))
            self.drawables.extend(list(self.portraits.values()))
            self.drawables.extend(list(self.landscapes.values()))
        
        # Create renpy object with width & height parameters
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            activity = self.get_selected_activity()

            is_lerp_complete = False
            elapsed_time = st - self.lerp_start_time

            # Ensure that elapsed_time is not greater than self.lerp_duration to avoid overshooting
            # OR just instantly skip there if the location for the activity is the same
            if elapsed_time >= self.lerp_duration or (self.x_current == activity.x and self.y_current == activity.y):
                self.x_current = activity.x
                self.y_current = activity.y
                is_lerp_complete = True
            else:
                progress_ratio = (elapsed_time / self.lerp_duration)
                eased_progress_ratio = 3 * progress_ratio ** 2 - 2 * progress_ratio ** 3

                self.x_current = self.x_cached + (activity.x - self.x_cached) * eased_progress_ratio
                self.y_current = self.y_cached + (activity.y - self.y_cached) * eased_progress_ratio
            
            render.place(self.map_drawable, x=self.x_current, y=self.y_current)
            render.place(self.bg_overlay, x=0, y=0)
            render.place(self.sidebar_drawable, x=30, y=35)
            render.place(self.sidebar_top_drawable, x=0, y=0)

            icon_x = 1080
            icon_y = 7
            render.place(self.icon_wireless, x=10, y=icon_y+3)
            render.place(self.icon_location, x=icon_x, y=icon_y+3)
            render.place(self.icon_bluetooth, x=icon_x+20, y=icon_y)
            render.place(self.icon_battery, x=icon_x+40, y=icon_y)

            render.place(self.top_text, x=50, y=9)
            render.place(Text(activity.location_name, xalign=0.5, yalign=0, font=self.get_font(), size=14), x=-120, y=5)

            if is_lerp_complete and not self.is_fading_out:
                render.place(self.beacon, x=activity.beacon_x, y=activity.beacon_y)

            # EMBARK BUTTON
            x_embark = 900
            y_embark = 550
            if self.selected_index < 0:
                render.place(self.btn_embark_d, x=x_embark, y=y_embark)
            elif self.is_unlocked(activity):
                render.place(self.btn_embark, x=x_embark, y=y_embark)
                if self.hovering_embark == True:
                    render.place(self.btn_embark_h, x=x_embark, y=y_embark)
            else:
                render.place(self.btn_locked, x=x_embark, y=y_embark)
                if self.hovering_embark == True:
                    render.place(self.btn_locked_h, x=x_embark, y=y_embark)

            # ACTIVITY LIST
            for act_idx in range(self.num_activities):
                x_diff = 20
                y_diff = act_idx*37

                # Large indent for the desc box
                if act_idx > self.selected_index and self.selected_index >= 0:
                    image_height = 225 if activity.description_bottom != "" else 100
                    y_diff += image_height

                if act_idx != self.hover_index:
                    render.place(self.bars[act_idx][0], x=x_diff, y=44+y_diff)
                # render.place(self.bars_points[act_idx], x=x_diff+268, y=50+y_diff)

                # Highlights
                if act_idx == self.selected_index:
                    desc_x=x_diff+40
                    desc_y=73+y_diff
                    if activity.description_bottom != "":
                        render.place(self.desc_box, x=desc_x, y=desc_y)
                        render.place(self.desc_box_highlight, x=desc_x, y=desc_y)
                    else:
                        render.place(self.desc_box_s, x=desc_x, y=desc_y)
                        render.place(self.desc_box_s_highlight, x=desc_x, y=desc_y)
                    
                    # Portrait/Landscape Mode
                    if activity.character != None:
                        if activity.character in self.portraits:
                            render.place(self.portrait_back, x=desc_x+15, y=desc_y+10)
                            render.place(self.portraits[activity.character], x=desc_x+18, y=desc_y+13)
                            render.place(Text(
                                activity.description_top, xalign=0, yalign=0, font=self.get_desc_font(), size=11, color='#b0c2c78e',outlines=[], xmaximum=120
                                ), x=desc_x+120, y=desc_y+15)
                        else:
                            if activity.description_bottom != "":
                                render.place(self.landscape_back, x=desc_x+22, y=desc_y+10)
                            render.place(self.landscapes[activity.character], x=desc_x+3+22, y=desc_y+13)
                    else:
                        top_y = 15 if activity.description_bottom != "" else 7
                        render.place(Text(
                            activity.description_top, xalign=0, yalign=0, font=self.get_desc_font(), size=11, color='#b0c2c78e',outlines=[], xmaximum=220
                            ), x=desc_x+15, y=desc_y+top_y)
                    render.place(Text(
                        activity.description_bottom, xalign=0, yalign=0, font=self.get_desc_font(), size=11, color='#b0c2c78e',outlines=[], xmaximum=220
                        ), x=desc_x+15, y=desc_y+133)
                if act_idx == self.hover_index:
                    render.place(self.bars[act_idx][1], x=x_diff, y=44+y_diff)
                    render.place(self.arrow, x=x_diff-19, y=52+y_diff)

                # Render text on top of everything
                render.place(self.bars_text[act_idx], x=x_diff+34, y=50+y_diff)

                # <EMBARK> was selected, fade-in a black screen (fake a fade-out effect)
                if self.is_fading_out:
                    elapsed_time = st - self.fade_time

                    if elapsed_time >= self.fade_duration:
                        alpha_value = 255  # Max alpha value
                    else:
                        alpha_value = int((elapsed_time / self.fade_duration) * 255) # round down

                    alpha_hex = hex(alpha_value)
                    alpha_hex = alpha_hex[2:]
                    if len(alpha_hex) >= 2 and self.fade_to_black: # fix single digits
                        render.place(Solid('#000000'+alpha_hex, xsize=1280, ysize=720), x=0, y=0)
                    if st > self.fade_time+self.fade_duration:
                        self.activity_ID = self.get_selected_activity().ID

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            y_min = 36 # width of 29 + (distance between of 14 divided by two to get 7)
            y_diff = 37
            activity = self.get_selected_activity()
            desc_height = 225 if activity.description_bottom != "" else 100

            # Hover over <EMBARK> button
            if x > 924 and y > 550 and y < 550+104:
                if self.hovering_embark == False and self.selected_index >= 0:
                    self.hovering_embark = True
                    renpy.play("gui/sfx/hover.ogg")
                    renpy.redraw(self, 0)
            else:
                if self.hovering_embark == True:
                    self.hovering_embark = False
                    renpy.redraw(self, 0)

            # Hover over locations list
            if x > 20 and x < 400 and y > y_min and y < y_min+self.num_activities*y_diff+desc_height:
                for act_idx in range(self.num_activities):

                    y_bonus = 0
                    # # Large indent for the desc box
                    if act_idx > self.selected_index and self.selected_index >= 0:
                        y_bonus += desc_height # image height

                    if act_idx == self.selected_index:
                        if y > y_min+act_idx*y_diff and y < y_min+(act_idx+1)*y_diff+desc_height:
                            if self.hover_index != act_idx:
                                self.hover_index = act_idx
                                renpy.play("gui/sfx/hover.ogg")
                                renpy.redraw(self, 0)
                    elif y > y_min+act_idx*y_diff+y_bonus and y < y_min+(act_idx+1)*y_diff+y_bonus:
                        if self.hover_index != act_idx:
                            self.hover_index = act_idx
                            renpy.play("gui/sfx/hover.ogg")
                            renpy.redraw(self, 0)
            else:
                self.hover_index = -1

            # Mouse Click
            if self.is_key_pressed(ev):
                if self.hover_index != -1 and self.selected_index != self.hover_index:
                    self.selected_index = self.hover_index
                    self.lerp_start_time = st
                    self.x_cached = self.x_current
                    self.y_cached = self.y_current
                    renpy.play("gui/sfx/select.ogg")
                    renpy.redraw(self, 0)
                if self.hovering_embark == True and self.selected_index >= 0 and self.is_unlocked(activity) and not self.is_fading_out:
                    self.is_fading_out = True
                    self.fade_time = st
                    renpy.play("gui/sfx/select.ogg")
                    renpy.redraw(self, 0)
            renpy.restart_interaction()

        def visit(self):
            return self.drawables

        def is_key_pressed(self, ev):
            if renpy.android:
                if ev.type == pygame.FINGERDOWN:
                    return True
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                return True
            return False

        def is_unlocked(self, activity):
            return activity.password == None or activity.password == persistent.chapel_unlocked 
            # hard coded, but whatever... (since it's not like the password feature is actually used)

        def get_font(self):
            return "mod_assets/map/font/LinkinPark-RifficFree-Bold.ttf"

        def get_desc_font(self):
            return "mod_assets/map/font/ModernDOS8x16.ttf"

        def get_selected_activity(self):
            return self.activity_list[self.selected_index] if self.selected_index >= 0 else self.activity_default

        def get_activity_list(self, activity_IDs):
            activity_list = []
            index = 0
            for a_ID in activity_IDs:
                for a in InteractiveMap.activity_tuples:
                    if a[0] == a_ID:
                        password = None if len(a) <= 11 else a[11]
                        activity_list.append(self.Activity(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], password))
                index += 1
            return activity_list

        class Activity:
            def __init__(self, ID, x, y, beacon_x, beacon_y, character, bar_variation, activity_name, location_name, description_top, description_bottom, password=None):
                self.ID = ID
                self.x = x
                self.y = y
                self.beacon_x = beacon_x
                self.beacon_y = beacon_y
                self.character = character
                self.bar_variation = bar_variation
                self.activity_name = activity_name
                self.location_name = location_name
                self.description_top = description_top
                self.description_bottom = description_bottom
                self.password = password

        class DummyActivity(Activity):
            def __init__(self, x, y, beacon_x, beacon_y, location_name):
                # lmao - imagine calling superclass constructor. couldn't be me!
                self.ID = "ID"
                self.x = x
                self.y = y
                self.beacon_x = beacon_x
                self.beacon_y = beacon_y
                self.character = None
                self.bar_variation = None
                self.activity_name = ""
                self.location_name = location_name
                self.description_top = ""
                self.description_bottom = ""
                self.password = None

        class Beacon(renpy.Displayable):
            def __init__(self, x, y):
                super(InteractiveMap.Beacon, self).__init__()
                self.x = x
                self.y = y
                self.point = Transform('mod_assets/map/beacon.png', zoom=.12)
                self.ring = Image('mod_assets/map/beacon_ring.png')
                self.cached_time = -1
                self.start_time = -1
                self.visible = True

                self.delay_time = 2

            def render(self, width, height, st, at):
                render = renpy.Render(width, height)

                if self.start_time <= 0:
                    self.start_time = st
                
                if self.visible:
                    elapsed_time = st - self.start_time

                    # Calculate the zoom_scale through a cubic interpolation
                    max_time = 1.0
                    cubic_interpolation = 3 * (elapsed_time / max_time) ** 2 - 2 * (elapsed_time / max_time) ** 3
                    zoom_scale = cubic_interpolation

                    # Ensure zoom_scale does not exceed 1
                    zoom_scale = min(zoom_scale, 1.0)
                    
                    r = 256
                    mult = .3
                    alpha = 1-(elapsed_time / max_time) ** 3
                    render.place(Transform(self.ring, zoom=.12+zoom_scale*mult, alpha=alpha), x=self.y-zoom_scale*mult*r, y=self.y-zoom_scale*mult*r)

                    if elapsed_time > max_time:
                        self.cached_time = st
                        self.visible = False
                else:
                    if st > self.cached_time + self.delay_time:
                        self.start_time = st
                        self.visible = True
                
                render.place(self.point, x=self.y, y=self.y)
                renpy.redraw(self, 0)
                return render