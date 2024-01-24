from tkinter import *
from pathlib import Path
from tkinter.font import Font


def relative_to_assets1(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame0")
    return ASSETS_PATH / Path(path)


def relative_to_assets2(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame1")
    return ASSETS_PATH / Path(path)


def relative_to_assets3(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame2")
    return ASSETS_PATH / Path(path)


def relative_to_assets4(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame3")
    return ASSETS_PATH / Path(path)

def relative_to_assets5(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame4")
    return ASSETS_PATH / Path(path)


def relative_to_assets6(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame5")
    return ASSETS_PATH / Path(path)


def relative_to_assets7(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyCharm\Tkinter-Designer\build\assets\frame6")
    return ASSETS_PATH / Path(path)


def create_interface1(root):
    frame1 = Frame(root, bg="#F3F3F3")
    frame1.pack(fill='both', expand=True)

    canvas = Canvas(
        frame1,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    global image_image_1
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets1("image_1.png"))
    canvas.create_image(
        787.0,
        250.0,
        image=image_image_1
    )

    global button_image_1
    button_image_1 = PhotoImage(file=relative_to_assets1("button_1.png"))
    button_1 = Button(
        frame1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface1),
        relief="flat"
    )
    button_1.place(
        x=74.0,
        y=104.0,
        width=306.0,
        height=67.0
    )

    global button_image_2
    button_image_2 = PhotoImage(file=relative_to_assets1("button_2.png"))
    button_2 = Button(
        frame1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface1),
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=450.0,
        width=250.0,
        height=67.0
    )

    canvas.create_text(
        74.0,
        201.0,
        anchor="nw",
        text="Lorem ipsum dolor sit amet consectetur. Eget nec adipiscing ipsum amet nunc quis placerat morbi nibh. Vestibulum eu iaculis in consequat sollicitudin habitant bibendum tincidunt donec. Eleifend.",
        fill="#414141",
        font=("Inter Medium", 25 * -1),
        width="400"
    )

    return frame1


def create_interface2(root):
    frame2 = Frame(root, bg="#F3F3F3")
    frame2.pack(fill='both', expand=True)

    canvas = Canvas(
        frame2,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        18.0,
        17.0,
        anchor="nw",
        text="Zdrowomix",
        fill="#414141",
        font=("Inter Bold", 55 * -1)
    )
    global image_image_1_1
    image_image_1_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))
    image_1 = canvas.create_image(
        929.0,
        106.0,
        image=image_image_1_1
    )

    canvas.create_rectangle(
        33.0,
        173.0,
        251.6883544921875,
        515.4514465332031,
        fill="#F9F9F9",
        outline="")

    global button_image_1_1
    button_image_1_1 = PhotoImage(
        file=relative_to_assets2("button_1.png"))
    button_1 = Button(
        frame2,
        image=button_image_1_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface3, interface2),
        relief="flat"
    )
    button_1.place(
        x=42.809814453125,
        y=464.618896484375,
        width=197.97975158691406,
        height=42.80643081665039
    )

    canvas.create_text(
        60.64581298828125,
        183.70166015625,
        anchor="nw",
        text="Kalkulator \nkalorii",
        fill="#414141",
        font=("Inter SemiBold", 25 * -1),
    )

    canvas.create_text(
        53.51141357421875,
        261.28826904296875,
        anchor="nw",
        text="Lorem ipsum dolor sit amet consectetur. Erat amet est lectus a ultrices non at ornare neque. Lacus neque rhoncus laoreet.",
        fill="#414141",
        font=("Inter Medium", 17 * -1),
        width="200",
        justify="center"
    )

    canvas.create_rectangle(
        271.307861328125,
        173.0,
        489.9962158203125,
        515.4514465332031,
        fill="#F9F9F9",
        outline="")

    global button_image_2_1
    button_image_2_1 = PhotoImage(
        file=relative_to_assets2("button_2.png"))
    button_2 = Button(
        frame2,
        image=button_image_2_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface5, interface2),
        relief="flat"
    )
    button_2.place(
        x=281.662353515625,
        y=464.618896484375,
        width=197.97975158691406,
        height=42.80643081665039
    )

    canvas.create_text(
        295.93115234375,
        183.70166015625,
        anchor="nw",
        text="Spis\nproduktów",
        fill="#414141",
        font=("Inter SemiBold", 25 * -1),
    )

    canvas.create_text(
        292.3638916015625,
        261.28826904296875,
        anchor="nw",
        text="Lorem ipsum dolor sit amet consectetur. Erat amet est lectus a ultrices non at ornare neque. Lacus neque rhoncus laoreet.",
        fill="#414141",
        font=("Inter Medium", 17 * -1),
        width="200",
        justify="center"
    )

    canvas.create_rectangle(
        509.6158447265625,
        173.0,
        728.30419921875,
        515.4514465332031,
        fill="#F9F9F9",
        outline="")

    global button_image_3_1
    button_image_3_1 = PhotoImage(
        file=relative_to_assets2("button_3.png"))
    button_3 = Button(
        frame2,
        image=button_image_3_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface6, interface2),
        relief="flat"
    )
    button_3.place(
        x=519.6229248046875,
        y=464.618896484375,
        width=197.97975158691406,
        height=42.80643081665039
    )

    canvas.create_text(
        535.67529296875,
        183.70166015625,
        anchor="nw",
        text="Porady\nżywieniowe",
        fill="#414141",
        font=("Inter SemiBold", 25 * -1),
    )

    canvas.create_text(
        531.21630859375,
        261.28826904296875,
        anchor="nw",
        text="Lorem ipsum dolor sit amet consectetur. Erat amet est lectus a ultrices non at ornare neque. Lacus neque rhoncus laoreet.",
        fill="#414141",
        font=("Inter Medium", 17 * -1),
        width="200",
        justify="center"
    )

    canvas.create_rectangle(
        748.0,
        173.0,
        966.6883544921875,
        515.4514465332031,
        fill="#F9F9F9",
        outline="")

    global button_image_4_1
    button_image_4_1 = PhotoImage(
        file=relative_to_assets2("button_4.png"))
    button_4 = Button(
        frame2,
        image=button_image_4_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface7, interface2),
        relief="flat"
    )
    button_4.place(
        x=758.007080078125,
        y=464.618896484375,
        width=197.97975158691406,
        height=42.80643081665039
    )

    canvas.create_text(
        774.0595703125,
        183.70166015625,
        anchor="nw",
        text="Sprawdź co\njesz!",
        fill="#414141",
        font=("Inter SemiBold", 25 * -1),
    )

    canvas.create_text(
        769.6005859375,
        261.28826904296875,
        anchor="nw",
        text="Lorem ipsum dolor sit amet consectetur. Erat amet est lectus a ultrices non at ornare neque. Lacus neque rhoncus laoreet.",
        fill="#414141",
        font=("Inter Medium", 17 * -1),
        width="200",
        justify="center"
    )

    return frame2


def create_interface3(root):
    frame3 = Frame(root, bg="#F3F3F3")
    frame3.pack(fill='both', expand=True)

    canvas = Canvas(
        frame3,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    global button_image_1_2
    canvas.place(x=0, y=0)
    button_image_1_2 = PhotoImage(
        file=relative_to_assets3("button_1.png"))
    button_1 = Button(
        frame3,
        image=button_image_1_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface3),
        relief="flat"
    )
    button_1.place(
        x=18.0,
        y=17.0,
        width=306.0,
        height=67.0
    )
    global button_image_2_2
    button_image_2_2 = PhotoImage(
        file=relative_to_assets3("button_2.png"))
    button_2 = Button(
        frame3,
        image=button_image_2_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface3),
        relief="flat"
    )
    button_2.place(
        x=829.0,
        y=-20.0,
        width=201.0,
        height=150.0
    )

    canvas.create_text(
        20.0,
        101.0,
        anchor="nw",
        text="Kalkulator kalorii \n",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    canvas.create_text(
        18.0,
        185.0,
        anchor="nw",
        text="Oblicz swoje zapotrzebowanie kaloryczne  sit amet consectetur. Volutpat et viverra varius enim vel sodales. Quis ullamcorper laoreet sed maecenas. Id ac ",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1),
        width="400"
    )

    canvas.create_text(
        466.0,
        255.0,
        anchor="nw",
        text="Waga:",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    global entry_image_1_2
    entry_image_1_2 = PhotoImage(
        file=relative_to_assets3("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        667.0,
        313.0,
        image=entry_image_1_2
    )
    entry_1 = Entry(
        frame3,
        bd=0,
        bg="#F9F9F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=465.0,
        y=294.0,
        width=404.0,
        height=36.0
    )

    canvas.create_text(
        466.0,
        442.0,
        anchor="nw",
        text="Płeć",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    global entry_image_2_2
    entry_image_2_2 = PhotoImage(
        file=relative_to_assets3("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        667.0,
        500.0,
        image=entry_image_2_2
    )
    entry_2 = Entry(
        frame3,
        bd=0,
        bg="#F9F9F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=465.0,
        y=481.0,
        width=404.0,
        height=36.0
    )

    canvas.create_text(
        466.0,
        159.0,
        anchor="nw",
        text="Wiek:",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    global entry_image_3_2
    entry_image_3_2 = PhotoImage(
        file=relative_to_assets3("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        667.0,
        217.0,
        image=entry_image_3_2
    )
    entry_3 = Entry(
        frame3,
        bd=0,
        bg="#F9F9F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=465.0,
        y=198.0,
        width=404.0,
        height=36.0
    )

    canvas.create_text(
        466.0,
        71.0,
        anchor="nw",
        text="Podaj imie:",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )
    global entry_image_4_2
    entry_image_4_2 = PhotoImage(
        file=relative_to_assets3("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        667.0,
        129.0,
        image=entry_image_4_2
    )
    entry_4 = Entry(
        frame3,
        bd=0,
        bg="#F9F9F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=465.0,
        y=110.0,
        width=404.0,
        height=36.0
    )
    global entry_image_5_2
    entry_image_5_2 = PhotoImage(
        file=relative_to_assets3("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        667.0,
        407.0,
        image=entry_image_5_2
    )
    entry_5 = Entry(
        frame3,
        bd=0,
        bg="#F9F9F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=465.0,
        y=388.0,
        width=404.0,
        height=36.0
    )

    canvas.create_text(
        466.0,
        350.0,
        anchor="nw",
        text="Aktywność",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        472.0,
        392.0,
        anchor="nw",
        text="słaba",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    global button_image_3_2
    button_image_3_2 = PhotoImage(
        file=relative_to_assets3("button_3.png"))
    button_3 = Button(
        frame3,
        image=button_image_3_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface4, interface3),
        relief="flat"
    )
    button_3.place(
        x=465.0,
        y=539.0,
        width=404.0,
        height=60.0
    )

    canvas.create_text(
        551.0,
        17.0,
        anchor="nw",
        text="Twoja dieta:",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    canvas.create_text(
        473.0,
        485.0,
        anchor="nw",
        text="mężczyzna\n",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    return frame3


def create_interface4(root):
    frame4 = Frame(root, bg="#F3F3F3")
    frame4.pack(fill='both', expand=True)

    canvas = Canvas(
        frame4,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global button_image_1_4
    button_image_1_4 = PhotoImage(
        file=relative_to_assets4("button_1.png"))
    button_1 = Button(
        frame4,
        image=button_image_1_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface4),
        relief="flat"
    )
    button_1.place(
        x=18.0,
        y=17.0,
        width=306.0,
        height=67.0
    )

    global button_image_2_4
    button_image_2_4 = PhotoImage(
        file=relative_to_assets4("button_2.png"))
    button_2 = Button(
        frame4,
        image=button_image_2_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface4),
        relief="flat"
    )
    button_2.place(
        x=829.0,
        y=18.0,
        width=201.0,
        height=177.0
    )

    canvas.create_text(
        20.0,
        101.0,
        anchor="nw",
        text="Kalkulator kalorii \n",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    canvas.create_text(
        102.0,
        159.0,
        anchor="nw",
        text="Twoje zapotrzebowanie kaloryczne wynosi : 10928kcal",
        fill="#414141",
        font=("Inter Medium", 30 * -1)
    )

    canvas.create_text(
        102.0,
        224.0,
        anchor="nw",
        text="zapotrzebowanie kaloryczne polega na czymś tam czymś tam jakiś opis czy cioś ds adasdsdadasdasda sdasdasdasdasdasdasdasdasdasdaarcu est sed convallis augue fusce. Id ultricies sem in at urna ",
        fill="#414141",
        font=("Inter Medium", 25 * -1),
        width="400"
    )

    global image_image_1_4
    image_image_1_4 = PhotoImage(
        file=relative_to_assets4("image_1.png"))
    image_1 = canvas.create_image(
        792.0,
        396.0,
        image=image_image_1_4
    )

    global button_image_3_4
    button_image_3_4 = PhotoImage(
        file=relative_to_assets4("button_3.png"))
    button_3 = Button(
        frame4,
        image=button_image_3_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface4),
        relief="flat"
    )
    button_3.place(
        x=102.0,
        y=484.0,
        width=276.0,
        height=60.0
    )
    return frame4


def create_interface5(root):
    frame5 = Frame(root, bg="#F3F3F3")
    frame5.pack(fill='both', expand=True)

    canvas = Canvas(
        frame5,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    global button_image_1_5
    button_image_1_5 = PhotoImage(
        file=relative_to_assets5("button_1.png"))
    button_1 = Button(
        frame5,
        image=button_image_1_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface5),
        relief="flat"
    )
    button_1.place(
        x=21.0078125,
        y=28.71484375,
        width=297.8369140625,
        height=42.87109375
    )
    global button_image_2_5
    button_image_2_5 = PhotoImage(
        file=relative_to_assets5("button_2.png"))
    button_2 = Button(
        frame5,
        image=button_image_2_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface5),
        relief="flat"
    )
    button_2.place(
        x=829.0,
        y=18.0,
        width=201.0,
        height=177.0
    )
    global entry_image_1_5
    entry_image_1_5 = PhotoImage(
        file=relative_to_assets5("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        578.5,
        51.0,
        image=entry_image_1_5
    )
    entry_1 = Entry(
        frame5,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=500.0,
        y=35.0,
        width=157.0,
        height=30.0
    )
    global button_image_3_5
    button_image_3_5 = PhotoImage(
        file=relative_to_assets5("button_3.png"))
    button_3 = Button(
        frame5,
        image=button_image_3_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=672.0,
        y=32.0,
        width=157.0,
        height=37.0
    )
    global image_image_1_5
    image_image_1_5 = PhotoImage(
        file=relative_to_assets5("image_1.png"))
    image_1 = canvas.create_image(
        774.0,
        375.0,
        image=image_image_1_5
    )

    canvas.create_text(
        20.0,
        101.0,
        anchor="nw",
        text="Spis produktów ",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    products = {"cytryna": ["dawd", "yviuj"], "jabłko": ["adwd", "kjhbk"], "cynamon": ["awd", "awd"],
                "arbuz": ["awda", "ohih8oi"], "melon": ["dawd", "wadad"], 'sad': ["wad", "wda"],
                'sadasd': ["wad", "awdwa"], 'asdawd': ["awd", "duabsuiok"]}

    product_listbox5 = Listbox(frame5, font=Font(size=30))
    scrollbar5 = Scrollbar(frame5, orient="vertical", command=product_listbox5.yview)
    product_listbox5.config(yscrollcommand=scrollbar5.set, selectforeground='#06982B', selectbackground='#F3F3F3')

    product_listbox5.place(x=28, y=185, width=250, height=350)
    scrollbar5.place(x=265, y=185, height=350)

    for product in products.keys():
        product_listbox5.insert("end", product)

    global button_image_4_5
    button_image_4_5 = PhotoImage(
        file=relative_to_assets5("button_4.png"))
    button_4 = Button(
        frame5,
        image=button_image_4_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=367.0,
        y=551.0,
        width=184.0,
        height=46.0
    )

    return frame5


def create_interface6(root):
    def update_product_info6(event):
        try:
            selection6 = product_listbox6.get(product_listbox6.curselection())
            # Aktualizacja informacji o produkcie
            # Tutaj możesz zastąpić to rzeczywistymi danymi dla każdego produktu
            product_info6.config(text=f"{selection6}\n{products[selection6][0]}")
            canvas.itemconfig(przepis, text=f"{products[selection6][1]}")
        except:
            pass
    frame6 = Frame(root, bg="#F3F3F3")
    frame6.pack(fill='both', expand=True)

    canvas = Canvas(
        frame6,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    global button_image_1_6
    button_image_1_6 = PhotoImage(
        file=relative_to_assets6("button_1.png"))
    button_1 = Button(
        frame6,
        image=button_image_1_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface6),
        relief="flat"
    )
    button_1.place(
        x=18.0,
        y=17.0,
        width=306.0,
        height=67.0
    )
    global button_image_2_6
    button_image_2_6 = PhotoImage(
        file=relative_to_assets6("button_2.png"))
    button_2 = Button(
        frame6,
        image=button_image_2_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface6),
        relief="flat"
    )
    button_2.place(
        x=829.0,
        y=18.0,
        width=201.0,
        height=109.0
    )

    global entry_image_1_6
    entry_image_1_6 = PhotoImage(
        file=relative_to_assets6("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        578.5,
        49.0,
        image=entry_image_1_6
    )
    entry_1 = Entry(
        frame6,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=500.0,
        y=31.0,
        width=157.0,
        height=34.0
    )

    global button_image_3_6
    button_image_3_6 = PhotoImage(
        file=relative_to_assets6("button_3.png"))
    button_3 = Button(
        frame6,
        image=button_image_3_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=672.0,
        y=31.0,
        width=157.0,
        height=38.0
    )

    canvas.create_text(
        20.0,
        101.0,
        anchor="nw",
        text="Sprawdź co jesz!",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    canvas.create_text(
        68.0,
        185.0,
        anchor="nw",
        text="Cebularz",
        fill="#06982B",
        font=("Inter SemiBold", 30 * -1)
    )

    canvas.create_rectangle(
        28.0,
        190.0,
        55.0,
        215.0,
        fill="#06982B",
        outline="")

    canvas.create_text(
        68.0,
        233.0,
        anchor="nw",
        text="Szarlotka",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1)
    )

    canvas.create_rectangle(
        28.0,
        238.0,
        55.0,
        263.0,
        fill="#06982B",
        outline="")

    canvas.create_text(
        68.0,
        281.0,
        anchor="nw",
        text="Cebulaki",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1)
    )

    canvas.create_rectangle(
        28.0,
        286.0,
        55.0,
        311.0,
        fill="#06982B",
        outline="")

    canvas.create_text(
        68.0,
        329.0,
        anchor="nw",
        text="Żylaki",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1)
    )

    canvas.create_rectangle(
        28.0,
        334.0,
        55.0,
        359.0,
        fill="#06982B",
        outline="")

    canvas.create_text(
        68.0,
        377.0,
        anchor="nw",
        text="Zupa z trupa",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1)
    )

    canvas.create_rectangle(
        28.0,
        382.0,
        55.0,
        407.0,
        fill="#06982B",
        outline="")

    products = {"cytryna": ["dawd", "yviuj"], "jabłko": ["adwd", "kjhbk"], "cynamon": ["awd", "awd"],
                "arbuz": ["awda", "ohih8oi"], "melon": ["dawd", "wadad"], 'sad': ["wad", "wda"],
                'sadasd': ["wad", "awdwa"], 'asdawd': ["awd", "duabsuiok"]}

    product_listbox6 = Listbox(frame6, font=Font(size=30))
    scrollbar6 = Scrollbar(frame6, orient="vertical", command=product_listbox6.yview)
    product_listbox6.config(yscrollcommand=scrollbar6.set, selectforeground='#06982B', selectbackground='#F3F3F3')

    product_listbox6.place(x=28, y=185, width=190, height=350)
    scrollbar6.place(x=215, y=185, height=350)

    for product in products.keys():
        product_listbox6.insert("end", product)

    product_info6 = Label(frame6, text="", font=("Inter SemiBold", 30), bg="#F3F3F3")
    product_info6.place(x=270, y=185, width=200, height=200)

    product_listbox6.bind("<<ListboxSelect>>", update_product_info6)
    product_listbox6.selection_set(0)

    global image_image_1_6
    image_image_1_6 = PhotoImage(
        file=relative_to_assets6("image_1.png"))
    image_1 = canvas.create_image(
        779.0,
        419.0,
        image=image_image_1_6
    )

    canvas.create_text(
        505.0,
        118.0,
        anchor="nw",
        text="Przepis:",
        fill="#414141",
        font=("Inter Medium", 35 * -1)
    )

    przepis = canvas.create_text(
        505.0,
        158.0,
        anchor="nw",
        text="Linkdoprzepisuhwdpjp100%.com",
        fill="#414141",
        font=("Inter Medium", 25 * -1)
    )

    return frame6


def create_interface7(root):
    def update_product_info7(event):
        try:
            selection = product_listbox7.get(product_listbox7.curselection())
            # Aktualizacja informacji o produkcie
            # Tutaj możesz zastąpić to rzeczywistymi danymi dla każdego produktu
            product_info7.config(text=f"{selection}\n{products[selection][0]}")
        except:
            pass

    frame7 = Frame(root, bg="#F3F3F3")
    frame7.pack(fill='both', expand=True)

    canvas = Canvas(
        frame7,
        bg="#F3F3F3",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global button_image_1_7
    button_image_1_7 = PhotoImage(
        file=relative_to_assets7("button_1.png"))
    button_1 = Button(
        frame7,
        image=button_image_1_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface7),
        relief="flat"
    )
    button_1.place(
        x=18.0,
        y=17.0,
        width=306.0,
        height=67.0
    )

    global button_image_2_7
    button_image_2_7 = PhotoImage(
        file=relative_to_assets7("button_2.png"))
    button_2 = Button(
        frame7,
        image=button_image_2_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(interface2, interface7),
        relief="flat"
    )
    button_2.place(
        x=829.0,
        y=-20,
        width=201.0,
        height=177.0
    )

    global entry_image_1_7
    entry_image_1_7 = PhotoImage(
        file=relative_to_assets7("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        578.5,
        51.0,
        image=entry_image_1_7
    )
    entry_1 = Entry(
        frame7,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=500.0,
        y=35.0,
        width=157.0,
        height=30.0
    )

    canvas.create_text(
        536.0,
        31.0,
        anchor="nw",
        text="wpisz",
        fill="#414141",
        font=("Inter SemiBold", 30 * -1)
    )

    global button_image_3_7
    button_image_3_7 = PhotoImage(
        file=relative_to_assets7("button_3.png"))
    button_3 = Button(
        frame7,
        image=button_image_3_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=672.0,
        y=31.0,
        width=157.0,
        height=38.0
    )

    canvas.create_text(
        20.0,
        101.0,
        anchor="nw",
        text="Sprawdź co jesz!",
        fill="#414141",
        font=("Inter SemiBold", 40 * -1)
    )

    global image_image_1_7
    image_image_1_7 = PhotoImage(
        file=relative_to_assets7("image_1.png"))
    image_1 = canvas.create_image(
        674.0,
        370.0,
        image=image_image_1_7
    )
    products = {"cytryna": ["dawd", "yviuj"], "jabłko": ["adwd", "kjhbk"], "cynamon": ["awd", "awd"],
                "arbuz": ["awda", "ohih8oi"], "melon": ["dawd", "wadad"], 'sad': ["wad", "wda"],
                'sadasd': ["wad", "awdwa"], 'asdawd': ["awd", "duabsuiok"]}

    product_listbox7 = Listbox(frame7, font=Font(size=30))
    scrollbar7 = Scrollbar(frame7, orient="vertical", command=product_listbox7.yview)
    product_listbox7.config(yscrollcommand=scrollbar7.set, selectforeground='#06982B', selectbackground='#F3F3F3')

    product_listbox7.place(x=28, y=185, width=190, height=350)
    scrollbar7.place(x=215, y=185, height=350)

    for product in products.keys():
        product_listbox7.insert("end", product)

    product_info7 = Label(frame7, text="", font=("Inter SemiBold", 30), bg="#F3F3F3")
    product_info7.place(x=270, y=185, width=200, height=200)

    product_listbox7.bind("<<ListboxSelect>>", update_product_info7)
    product_listbox7.selection_set(0)

    return frame7


# Funkcja do przełączania ramki
def switch_frame(frame_to_show, frame_to_hide):
    frame_to_hide.pack_forget()  # Ukryj nieaktywną ramkę
    frame_to_show.pack(fill='both', expand=True)


# Główne okno aplikacji
window = Tk()
window.geometry("1000x600")
window.configure(bg="#F3F3F3")
window.title('Zdrowomix')

# Tworzenie interfejsów
# Start interfejs
interface1 = create_interface1(window)
# Menu wyboru usługi
interface2 = create_interface2(window)
# Kalkulator BMI
interface3 = create_interface3(window)
interface3.pack_forget()
# Wynik BMI
interface4 = create_interface4(window)
interface4.pack_forget()

interface5 = create_interface5(window)
interface5.pack_forget()

interface6 = create_interface6(window)
interface6.pack_forget()

interface7 = create_interface7(window)
interface7.pack_forget()

# Ustawienie domyślnego interfejsu
switch_frame(interface1, interface2)
window.resizable(False, False)
window.mainloop()
