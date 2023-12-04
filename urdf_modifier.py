from tkinter import *
from tkinter.ttk import *
from modify_worker import *
from simulation_visualization import *
import os
from threading import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


class HumanoidModifier:
    # Default URDF files
    worker_urdf = 'factory_worker.urdf'
    default_urdf = 'factory_worker_default.urdf'
    urdf_models = {'factory_worker.urdf': 0}
    urdf_model_heights = {'factory_worker.urdf': 1.3}
    # Array with human dimensions
    body_dimensions, body_radius, body_mass, body_part_length, body_part_radius, body_part_mass = [], [], [], [], [], []

    def __init__(self):
        # Start App
        self.init_ui()

    def __del__(self):
        print('URDF mofifier finished')

    def update_urdf(self):
        # Round values to 5 decimal digits and format them
        file_to_update = './workers/' + str(self.worker_urdf)
        if (file_to_update != './workers/factory_worker_default.urdf'):
            for i in range(12):
                self.body_part_length[i] = str(
                    format(round(self.body_dimensions[i].get(), 5), '.5f'))
                self.body_part_radius[i] = str(
                    format(round(self.body_radius[i].get(), 5), '.5f'))
                self.body_part_mass[i] = str(
                    format(round(self.body_mass[i].get(), 5), '.5f'))
            # Update URDF
            set_humanoid_urdf(self.body_part_length, self.body_part_radius,
                              self.body_part_mass, self.worker_urdf)
            # Set model height
            left_leg = float(
                self.body_part_length[6]) + float(self.body_part_length[7])
            right_leg = float(
                self.body_part_length[9]) + float(self.body_part_length[10])
            model_height = left_leg + 0.69
            if (right_leg > left_leg):
                model_height = right_leg + 0.69
            self.urdf_model_heights.update(
                {str(self.worker_urdf): model_height})
        else:
            showinfo('Success', 'You can not update default URDF file.')

    def visualization_simulation(self):
        # Hide main window UI
        self.master.withdraw()
        # Run visualization
        simulation_visualization(
            self.worker_urdf,
            self.urdf_model_heights[self.worker_urdf]
        )
        showinfo('Visualization finished', 'Simulation has finished.')
        # Unhide main window UI
        self.master.deiconify()

    def restore_urdf(self):
        # Read default URDF
        tree = ET.parse('./workers/factory_worker_default.urdf')
        # Restore URDF
        tree.write('./workers/' + str(self.worker_urdf), pretty_print=True)
        # Get URDF values
        self.body_part_length, self.body_part_radius, self.body_part_mass = get_humanoid_urdf(
            self.worker_urdf)
        # Update variables and UI
        for i in range(12):
            self.body_dimensions[i].set(self.body_part_length[i])
            self.body_radius[i].set(self.body_part_radius[i])
            self.body_mass[i].set(self.body_part_mass[i])
        # Set model height
        left_leg = float(
            self.body_part_length[6]) + float(self.body_part_length[7])
        right_leg = float(
            self.body_part_length[9]) + float(self.body_part_length[10])
        model_height = left_leg + 0.69
        if (right_leg > left_leg):
            model_height = right_leg + 0.69
        self.urdf_model_heights.update({str(self.worker_urdf): model_height})

    def remove_urdf(self):
        file_to_remove = './workers/' + str(self.worker_urdf)
        if (file_to_remove != './workers/factory_worker_default.urdf'):
            os.remove(file_to_remove)
            showinfo('Success', 'URDF with name ' +
                     str(self.worker_urdf) + ' removed.')
            # Get list of URDF
            self.options = self.file_explorer()
            self.combo['values'] = self.options
            # Set primary URDF
            self.worker_urdf = str(self.options[0])
            self.selected_urdf.set(self.worker_urdf)
            self.info.set(self.worker_urdf)
            # Get URDF values
            self.body_part_length, self.body_part_radius, self.body_part_mass = get_humanoid_urdf(
                self.worker_urdf)
            # Update variables and UI
            for i in range(12):
                self.body_dimensions[i].set(self.body_part_length[i])
                self.body_radius[i].set(self.body_part_radius[i])
                self.body_mass[i].set(self.body_part_mass[i])
        else:
            showinfo('Success', 'You can not remove default URDF file.')

    def file_explorer(self):
        urdf_files = []
        path = 'workers'
        files = os.listdir(path)
        for file in files:
            urdf_files.append(file)
            self.urdf_models.update({str(file): 0})
            self.urdf_model_heights.update({str(file): 1.3})
        return urdf_files

    def set_legs_state(self, state):
        set_fixed_legs(state, self.selected_urdf.get())

    def option_changed(self, _):
        # Get URDF values
        self.worker_urdf = self.selected_urdf.get()
        self.info.set(self.worker_urdf)
        self.body_part_length, self.body_part_radius, self.body_part_mass = get_humanoid_urdf(
            self.selected_urdf.get())
        # Update variables and UI
        for i in range(12):
            self.body_dimensions[i].set(self.body_part_length[i])
            self.body_radius[i].set(self.body_part_radius[i])
            self.body_mass[i].set(self.body_part_mass[i])
        # Edit checkbox
        self.in_simulation.set(self.urdf_models[str(self.worker_urdf)])
        self.model_selection()

    def add_worker(self):
        name = askstring('URDF Name', 'What is the name of the URDF?')
        path = './workers/'
        if (name != None):
            tree = ET.parse('./workers/' + str(self.default_urdf))
            showinfo('Success', 'URDF with name ' + str(name) + ' added.')
            # Update the modified URDF file
            tree.write(path + str(name) + '.urdf', pretty_print=True)
            # Get list of URDF
            self.options = self.file_explorer()
            self.combo['values'] = self.options
            # Set primary URDF
            self.worker_urdf = str(name) + '.urdf'
            self.selected_urdf.set(self.worker_urdf)
            self.info.set(self.worker_urdf)
        else:
            showinfo('Success', 'Give a valid name!')

    def model_selection(self):
        self.urdf_models.update(
            {str(self.worker_urdf): self.in_simulation.get()})
        # Set model height
        left_leg = float(
            self.body_part_length[6]) + float(self.body_part_length[7])
        right_leg = float(
            self.body_part_length[9]) + float(self.body_part_length[10])
        model_height = left_leg + 0.69
        if (right_leg > left_leg):
            model_height = right_leg + 0.69
        self.urdf_model_heights.update({str(self.worker_urdf): model_height})
        # Set model counter
        counter = 0
        for urdf in self.urdf_models:
            counter = counter + self.urdf_models[urdf]

    def init_ui(self):
        # Start App
        self.master = Tk()
        self.master.title('FELICE - Humanoid URDF Modifier')
        self.master.geometry('1250x600')
        self.master.iconphoto(False, PhotoImage(file='./images/logo.png'))
        # Create scrollable frame
        container = Frame(self.master)
        container.pack(fill='both', expand=True)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        canvas_m = Canvas(container, highlightthickness=0)
        scr_y = AutoScrollbar(container, orient=VERTICAL)
        scr_x = AutoScrollbar(container, orient=HORIZONTAL)
        scr_y.config(command=canvas_m.yview)
        scr_x.config(command=canvas_m.xview)
        self.mst = Frame(canvas_m)
        fc = canvas_m.create_window((0, 0), window=self.mst, anchor='nw')
        canvas_m.configure(yscrollcommand=scr_y.set)
        canvas_m.configure(xscrollcommand=scr_x.set)

        def on_canvas_resize(event):
            x = (event.width - self.mst.winfo_width()) / 2
            canvas_m.coords(fc, (x, 0))
            bbox = (0, 0, self.mst.winfo_width(), self.mst.winfo_height())
            canvas_m.config(scrollregion=bbox)

        canvas_m.bind('<Configure>', on_canvas_resize)
        canvas_m.grid(row=0, column=0, sticky=NSEW)
        # X and Y scrollbars of overflow
        scr_y.grid(row=0, column=1, sticky=NSEW)
        scr_x.grid(row=1, column=0, sticky=NSEW)
        # UI Frames
        info_frame = Frame(self.mst)
        info_frame.pack()
        Separator(self.mst, orient='horizontal').pack(fill='x', pady=10)
        center_frame = Frame(self.mst)
        center_frame.pack()
        dash_frame = Frame(center_frame)
        dash_frame.pack(side=LEFT)
        image_frame = Frame(center_frame)
        image_frame.pack(side=RIGHT, padx=100)
        Separator(self.mst, orient='horizontal').pack(fill='x', pady=10)
        center_buttons_frame = Frame(self.mst)
        center_buttons_frame.pack()
        buttons_frame_urdf = Frame(center_buttons_frame)
        buttons_frame_urdf.pack(side=LEFT, fill='y', padx=30)
        buttons_frame_simulation = Frame(center_buttons_frame)
        buttons_frame_simulation.pack(side=RIGHT, fill='y', padx=30)

        # Get URDF values
        if (os.path.isfile('./workers/' + str(self.worker_urdf)) == False):
            self.worker_urdf = self.default_urdf
        self.body_part_length, self.body_part_radius, self.body_part_mass = get_humanoid_urdf(
            self.worker_urdf)

        # Fill with zeros
        for i in range(12):
            self.body_dimensions.append(DoubleVar())
            self.body_dimensions[i].set(0)
            self.body_radius.append(DoubleVar())
            self.body_radius[i].set(0)
            self.body_mass.append(DoubleVar())
            self.body_mass[i].set(0)

        # Array with human dimensions
        for i in range(12):
            self.body_dimensions.append(DoubleVar())
            self.body_dimensions[i].set(self.body_part_length[i])
            self.body_radius.append(DoubleVar())
            self.body_radius[i].set(self.body_part_radius[i])
            self.body_mass.append(DoubleVar())
            self.body_mass[i].set(self.body_part_mass[i])

        # Info label
        self.info = StringVar()
        self.info.set(self.worker_urdf)
        Label(info_frame, text='Worker: ').grid(row=0, column=0)
        Label(info_frame, textvariable=self.info).grid(row=0, column=1)
        # Hand
        Label(dash_frame, text='Left arm (length m./mass kg/radius m.): ').grid(row=0,
                                                                                column=0, sticky=W)
        Label(dash_frame, text='Left forearm (length m./mass kg/radius m.): ').grid(row=1,
                                                                                    column=0, sticky=W)
        Label(dash_frame, text='Left wrist palm (length m./mass kg/radius m.): ').grid(
            row=2, column=0, sticky=W)
        Label(dash_frame, text='Right arm (length m./mass kg/radius m.): ').grid(row=3,
                                                                                 column=0, sticky=W)
        Label(dash_frame, text='Right forearm (length m./mass kg/radius m.): ').grid(
            row=4, column=0, sticky=W)
        Label(dash_frame, text='Right wrist palm (length m./mass kg/radius m.): ').grid(
            row=5, column=0, sticky=W)
        # Leg
        Label(dash_frame, text='Left thigh (length m./mass kg/radius m.): ').grid(row=6,
                                                                                  column=0, sticky=W)
        Label(dash_frame, text='Left leg (length m./mass kg/radius m.): ').grid(row=7,
                                                                                column=0, sticky=W)
        Label(dash_frame, text='Left foot (length m./mass kg/radius m.): ').grid(row=8,
                                                                                 column=0, sticky=W)
        Label(dash_frame, text='Right thigh (length m./mass kg/radius m.): ').grid(row=9,
                                                                                   column=0, sticky=W)
        Label(dash_frame, text='Right leg (length m./mass kg/radius m.): ').grid(row=10,
                                                                                 column=0, sticky=W)
        Label(dash_frame, text='Right foot (length m./mass kg/radius m.): ').grid(row=11,
                                                                                  column=0, sticky=W)
        # Body dimensions values
        Entry(dash_frame, textvariable=self.body_dimensions[0], width=10).grid(
            row=0, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[1], width=10).grid(
            row=1, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[2], state='disabled', width=10).grid(
            row=2, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[3], width=10).grid(
            row=3, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[4], width=10).grid(
            row=4, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[5], state='disabled', width=10).grid(
            row=5, column=1, sticky=W, pady=4)
        # Leg
        Entry(dash_frame, textvariable=self.body_dimensions[6], width=10).grid(
            row=6, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[7], width=10).grid(
            row=7, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[8], state='disabled', width=10).grid(
            row=8, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[9], width=10).grid(
            row=9, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[10], width=10).grid(
            row=10, column=1, sticky=W, pady=4)
        Entry(dash_frame, textvariable=self.body_dimensions[11], state='disabled', width=10).grid(
            row=11, column=1, sticky=W, pady=4)
        # Body dimensions
        Scale(dash_frame, variable=self.body_dimensions[0], from_=0.01, to=2.0).grid(
            row=0, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[1], from_=0.01, to=2.0).grid(
            row=1, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[2], from_=0.01, to=2.0, state='disabled').grid(
            row=2, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[3], from_=0.01, to=2.0).grid(
            row=3, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[4], from_=0.01, to=2.0).grid(
            row=4, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[5], from_=0.01, to=2.0, state='disabled').grid(
            row=5, column=2, sticky=W, pady=4)
        # Leg
        Scale(dash_frame, variable=self.body_dimensions[6], from_=0.01, to=2.0).grid(
            row=6, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[7], from_=0.01, to=2.0).grid(
            row=7, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[8], from_=0.01, to=2.0, state='disabled').grid(
            row=8, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[9], from_=0.01, to=2.0).grid(
            row=9, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[10], from_=0.01, to=2.0).grid(
            row=10, column=2, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_dimensions[11], from_=0.01, to=2.0, state='disabled').grid(
            row=11, column=2, sticky=W, pady=4)
        # Body masses values
        Entry(dash_frame, textvariable=self.body_mass[0], width=10).grid(
            row=0, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[1], width=10).grid(
            row=1, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[2], width=10).grid(
            row=2, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[3], width=10).grid(
            row=3, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[4], width=10).grid(
            row=4, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[5], width=10).grid(
            row=5, column=3, sticky=W, padx=4)
        # Leg
        Entry(dash_frame, textvariable=self.body_mass[6], width=10).grid(
            row=6, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[7], width=10).grid(
            row=7, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[8], width=10).grid(
            row=8, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[9], width=10).grid(
            row=9, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[10], width=10).grid(
            row=10, column=3, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_mass[11], width=10).grid(
            row=11, column=3, sticky=W, padx=4)
        # Body masses
        Scale(dash_frame, variable=self.body_mass[0], from_=0.01, to=5.0).grid(
            row=0, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[1], from_=0.01, to=5.0).grid(
            row=1, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[2], from_=0.01, to=5.0).grid(
            row=2, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[3], from_=0.01, to=5.0).grid(
            row=3, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[4], from_=0.01, to=5.0).grid(
            row=4, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[5], from_=0.01, to=5.0).grid(
            row=5, column=4, sticky=W, pady=4)
        # Leg
        Scale(dash_frame, variable=self.body_mass[6], from_=0.01, to=5.0).grid(
            row=6, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[7], from_=0.01, to=5.0).grid(
            row=7, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[8], from_=0.01, to=5.0).grid(
            row=8, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[9], from_=0.01, to=5.0).grid(
            row=9, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[10], from_=0.01, to=5.0).grid(
            row=10, column=4, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_mass[11], from_=0.01, to=5.0).grid(
            row=11, column=4, sticky=W, pady=4)
        # Body parts radius values
        Entry(dash_frame, textvariable=self.body_radius[0], width=10).grid(
            row=0, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[1], width=10).grid(
            row=1, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[2], width=10).grid(
            row=2, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[3], width=10).grid(
            row=3, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[4], width=10).grid(
            row=4, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[5], width=10).grid(
            row=5, column=5, sticky=W, padx=4)
        # Leg
        Entry(dash_frame, textvariable=self.body_radius[6], width=10).grid(
            row=6, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[7], width=10).grid(
            row=7, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[8], width=10).grid(
            row=8, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[9], width=10).grid(
            row=9, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[10], width=10).grid(
            row=10, column=5, sticky=W, padx=4)
        Entry(dash_frame, textvariable=self.body_radius[11], width=10).grid(
            row=11, column=5, sticky=W, padx=4)
        # Body parts radius
        Scale(dash_frame, variable=self.body_radius[0], from_=0.01, to=0.2).grid(
            row=0, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[1], from_=0.01, to=0.2).grid(
            row=1, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[2], from_=0.01, to=0.2).grid(
            row=2, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[3], from_=0.01, to=0.2).grid(
            row=3, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[4], from_=0.01, to=0.2).grid(
            row=4, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[5], from_=0.01, to=0.2).grid(
            row=5, column=6, sticky=W, pady=4)
        # Leg
        Scale(dash_frame, variable=self.body_radius[6], from_=0.01, to=0.2).grid(
            row=6, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[7], from_=0.01, to=0.2).grid(
            row=7, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[8], from_=0.01, to=0.2).grid(
            row=8, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[9], from_=0.01, to=0.2).grid(
            row=9, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[10], from_=0.01, to=0.2).grid(
            row=10, column=6, sticky=W, pady=4)
        Scale(dash_frame, variable=self.body_radius[11], from_=0.01, to=0.2).grid(
            row=11, column=6, sticky=W, pady=4)
        Button(dash_frame, text='Set Fixed Legs', command=lambda: self.set_legs_state(
            True), width=16).grid(row=12, column=3, sticky=S, pady=4)
        Button(dash_frame, text='Set Revolute Legs', command=lambda: self.set_legs_state(
            False), width=16).grid(row=12, column=4, sticky=S, pady=4)
        # Dropdown menu options
        self.selected_urdf = StringVar()
        self.selected_urdf.set(self.worker_urdf)
        self.combo = Combobox(
            buttons_frame_urdf,
            textvariable=self.selected_urdf,
            width=30,
            state='readonly'
        )
        self.combo.bind('<<ComboboxSelected>>', self.option_changed)
        self.combo['values'] = self.file_explorer()
        # Set model height
        left_leg = float(
            self.body_part_length[6]) + float(self.body_part_length[7])
        right_leg = float(
            self.body_part_length[9]) + float(self.body_part_length[10])
        model_height = left_leg + 0.69
        if (right_leg > left_leg):
            model_height = right_leg + 0.69
        self.urdf_model_heights.update({str(self.worker_urdf): model_height})
        self.combo.grid(row=0, column=0, sticky=S, pady=4, padx=10)
        self.in_simulation = IntVar()
        self.in_simulation.set(1)
        self.urdf_models.update({str(self.worker_urdf): 1})
        Button(buttons_frame_urdf, text='Add Worker', command=self.add_worker,
               width=20).grid(row=0, column=1, sticky=S, pady=4)
        # Action buttons left
        Button(buttons_frame_urdf, text='Update URDF', command=self.update_urdf,
               width=20).grid(row=1, column=2, sticky=S, pady=4)
        Button(buttons_frame_urdf, text='Restore URDF', command=self.restore_urdf,
               width=20).grid(row=1, column=1, sticky=S, pady=4)
        Button(buttons_frame_urdf, text='Remove URDF', command=self.remove_urdf,
               width=20).grid(row=0, column=2, sticky=S, pady=4)
        Button(buttons_frame_urdf, text='Visualize data',
               command=self.visualization_simulation, width=20).grid(row=0, column=3)
        # Genetic algorithm
        genetic_frame = Frame(buttons_frame_urdf)
        genetic_frame.grid(row=4, columnspan=3, sticky=W, padx=10, pady=15)
        # Humanoid image
        canvas = Canvas(image_frame, width=216, height=400)
        canvas.pack()
        img = PhotoImage(file='./images/humanoid.png')
        canvas.create_image(108, 200, image=img)
        mainloop()


class AutoScrollbar(Scrollbar):
    # Defining set method with all its parameter
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            # Using grid_remove
            self.tk.call('grid', 'remove', self)
        else:
            self.grid()
        Scrollbar.set(self, low, high)

    # Defining pack method
    def pack(self, **kw):
        # If pack is used it throws an error
        raise (TclError, 'pack cannot be used with this widget')

    # Defining place method
    def place(self, **kw):
        # If place is used it throws an error
        raise (TclError, 'place cannot be used  with this widget')


def main():
    try:
        HumanoidModifier()
    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print('Keyboard Interrupt...')


if __name__ == '__main__':
    main()
