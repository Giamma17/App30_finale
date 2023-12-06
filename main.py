import flet as f 

#colori
def main(page: f.Page):
    BG = '#041955' #blu scuro
    FWG = '#97b4ff' #ciano
    FG = '#3450a1' #ciano scuro
    theme = f.Theme()
    theme.visual_density = f.ThemeVisualDensity.COMPACT
    page.theme_mode = f.ThemeMode.DARK
    page.window_width = 350        # window's width is 200 px
    page.window_height = 200       # window's height is 200 px
    page.window_resizable = True  # window is not resizable
    page.update()
    page.window_width = 600        # window's width is 400 px
    page.window_height = 400       # window's height is 400 px
    page.window_resizable = True  # window is not resizable
    page.update()
    page.scroll = "auto"
    page.icon = "icona.png"
    page.update()
    
    #funzionamento source bar
    data = [
		{
			"name":"john","age":12
		},
		{
			"name":"oppw","age":12
		},
		{
			"name":"jenifer","age":12
		},
		{
			"name":"aaan","age":12
		},
		{
			"name":"buyua","age":12
		},
		{
			"name":"qwmiu","age":12
		},
		{
			"name":"dokoo","age":12
		},

	]
    resultdata = f.ListView()
    resultcon = f.Container(
		bgcolor="#041955",
		padding=10,
		margin=10,
        border_radius=20,
		offset=f.transform.Offset(-2,0),
		animate_offset = f.animation.Animation(600,curve="easeIn"),
		content=f.Column([
			resultdata
			])
		)
    def searchnow(e):
        mysearch = e.control.value
        result = []

		# IF NOT BLANK YOU TEXTFIELD SEARCH THE RUN FUNCTION
        if not mysearch == "":
            resultcon.visible = True
            for item in data:
                if mysearch in item['name']:
                    resultcon.offset = f.transform.Offset(0,0)
                    result.append(item)
            page.update()

		# IF RESULT THERE DATA THEN PUSH DATA TO WIDGET CONTAINER Resultcon
        if result:
            resultdata.controls.clear()
            for x in result:
                resultdata.controls.append(
                    f.FloatingActionButton(
                            icon = f.icons.MENU, on_click=lambda _: page.go('/create_task3'),
                        ),
						size=20,color="#97b4ff"
						)
            page.update()
        else:
            resultcon.offset = f.transform.Offset(-2,0)
            resultdata.controls.clear()
            page.update()

    resultcon.visible = False
    txtsearch = f.TextField(label="Scrivi qui",
		on_change=searchnow
		)
    

#scrollo le categorie
    categories_card = f.Row(
        scroll= 'auto'
    )
    categories = ['Leggi','Gioca','Shop']

#creo la prima vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[0]),
                        f.FloatingActionButton(
                            icon = f.icons.ADD, on_click=lambda _: page.go('/create_task'),
                        ),
                    ]
                )

            )
        )

#creo la seconda vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[1]),
                        f.FloatingActionButton(
                            icon = f.icons.SEARCH, on_click=lambda _: page.go('/create_task2'),
                        ),
                    ]
                )

            )
        )

#creo la terza vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[2]),
                        f.FloatingActionButton(
                            icon = f.icons.MENU, on_click=lambda _: page.go('/create_task3'),
                        ),
                    ]
                )

            )
        )

#content pagina 1 con le slide
    create_task_view = f.Container(
        content = f.Container(
            height = 80,
            width =80,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )

#content pagina 2 con il quiz
    create_task_view2 = f.Container(
        content = f.Container(
            height = 80,
            width =80,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )

#content pagina 3 con lo shop
    create_task_view3 = f.Container(
        content = f.Container(
            height = 80,
            width =80,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )
    
#content pagina 3 con il search
    search_box = f.Container(
        content =f.Column(
        controls =[
            f.Container(
            height = 20,
            width =50,
            content=f.Text('<-----',size =10),
            on_click=lambda _: page.go('/'),
            ),
            f.Column([
                f.Text("Cerca",size = 20,weight="bold"),
                txtsearch,
                resultcon
                ]),
            f.Container(
                    padding=f.padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content = categories_card
                ),
        ]
        )
        
    )
    

#content della home
    home_page_contents = f.Container(
        content=f.Column(
            controls=[
                f.Row(alignment='spaceBetween',
                    controls=[
                        f.Container(
                            content=f.Icon(
                                f.icons.MENU)),

                        f.Container(
                            f.Icon(f.icons.SEARCH),
                            on_click =lambda _: page.go('/search'),
                        )
                            

                    ]
                ),
                f.Text(value="Ciao"),
                f.Text(value="CATEGORIES"),
                f.Container(
                    padding=f.padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content = categories_card
                ),

                    f.Text(value = " Credits:  Gianmarco Lugaresi"),
                
                
            ],
        ),
    )

#se voglio creare una colonna di cose nella pagina principale
    tasks = f.Column(
    )

#funziamento e granezza pagine
    page_2 = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius= 20,
                padding=f.padding.only(
                    top=45,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        home_page_contents
                    ]
                )
            )
        ]
    )
    slide = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right= 30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view
                    ]
                )
            )
        ]
    )
    game = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view2
                    ]
                )
            )
        ]
    )
    shop = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view3
                    ]
                )
            )
        ]
    )
    search = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        search_box
                    ]
                )
            )
        ]
    )
#sfondo home
    container = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                page_2,
            ]  
        )
    )

#sfondo slide
    container_slide = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                slide,
            ]  
        )
    )
#sfondo mini-game
    container_game = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                game,
            ]  
        )
    )
#sfondo shop
    container_shop = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                shop,
            ]  
        )
    )
#sfondo search_box
    search_page = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                search,
            ]  
        )
    )


#dizionari per muoversi nelle pagine
    pages = {
        '/': f.View(
            "/",
            [
                container
            ],
        ),
        '/create_task': f.View(
            "/create_task",
            [
                container_slide
            ],
        ),

        '/create_task2': f.View(
            "/create_task2",
            [
                container_game
            ],
        ),
        '/create_task3': f.View(
            "/create_task3",
            [
                container_shop
            ],
        ),
        '/search': f.View(
            "/search",
            [
                search_page
            ],
        ),
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.on_route_change = route_change
    page.go(page.route)

f.app(target=main)
