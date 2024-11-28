import tkinter as tk

class MultiWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Marketplace")

        self.home_frame = HomePage(self.root, self)
        self.customer_frame = Customer(self.root, self)
        self.seller_frame = Seller(self.root, self)
        self.sign_up_frame = Sign_up(self.root, self)
        self.customer_page_frame = Customer_page(self.root, self)
        self.seller_page_frame = Seller_page(self.root, self)
        self.mistake_frame = Mistake(self.root, self)
        self.success_frame = Success(self.root, self)


        self.show_frame(self.home_frame)

    def show_frame(self, frame):
        self.home_frame.pack_forget()
        self.customer_frame.pack_forget()
        self.seller_frame.pack_forget()
        self.sign_up_frame.pack_forget()
        self.customer_page_frame.pack_forget()
        self.seller_page_frame.pack_forget()
        self.mistake_frame.pack_forget()
        self.success_frame.pack_forget()
        
        frame.pack(fill='both', expand=True)
    
    def show_mistake(self):
        self.mistake_frame.pack(fill='both', expand=True)

    def close_mistake(self):
        self.mistake_frame.pack_forget()
    
    def show_success(self):
        self.success_frame.pack(fill='both', expand=True)

    def close_success(self):
        self.success_frame.pack_forget()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        button1 = tk.Button(self, text="Войти как покупатель",
                            command=lambda: self.controller.show_frame(self.controller.customer_frame),
                            font=("Courier", 24))
        button1.pack(padx=80, pady=5)

        button1 = tk.Button(self, text="Войти как продавец",
                            command=lambda: self.controller.show_frame(self.controller.seller_frame),
                            font=("Courier", 24))
        button1.pack(padx=80, pady=5)

        button2 = tk.Button(self, text="Регистрация",
                            command=lambda: self.controller.show_frame(self.controller.sign_up_frame),
                            font=("Courier", 24))
        button2.pack(padx=80, pady=30)

class Customer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def entr(self, entry):
        flag = 0
        with open('data_customers.txt', 'r') as keys:
            lines = keys.readlines()
            for line in lines:
                if (entry.get() == line[:-1]):
                    self.controller.show_frame(self.controller.customer_page_frame)
                    flag = 1
                    break
                line = keys.readline()
        if (flag == 0):
            self.controller.show_mistake()

    def create_widgets(self):
        label = tk.Label(self, text="Вход", font=("Courier", 24))
        label.pack(pady=10)
        label = tk.Label(self, text="Введите данные покупателя", font=("Courier", 14))
        label.pack(pady=10)

        entry = tk.Entry(self, width=25)
        entry.pack(pady=20)
        button = tk.Button(self, text="Войти", bg="green", activebackground="darkgreen",
                           font=("Courier", 24), command=lambda: self.entr(entry))
        button.pack(pady=5)

        button = tk.Button(self, text="Назад на главную", bg="red", activebackground="darkred",
                           command=lambda: self.controller.show_frame(self.controller.home_frame),
                           font=("Courier", 24))
        button.pack(pady=5)

class Seller(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def entr(self, entry):
        flag = 0
        with open('data_sellers.txt', 'r') as keys:
            lines = keys.readlines()
            for line in lines:
                if (entry.get() == line[:-1]):
                    self.controller.show_frame(self.controller.seller_page_frame)
                    flag = 1
                    break
                line = keys.readline()
        if (flag == 0):
            self.controller.show_mistake()

    def create_widgets(self):
        label = tk.Label(self, text="Вход", font=("Courier", 24))
        label.pack(pady=10)
        label = tk.Label(self, text="Введите данные продавца", font=("Courier", 14))
        label.pack(pady=10)

        entry = tk.Entry(self, width=25)
        entry.pack(pady=20)
        button = tk.Button(self, text="Войти", bg="green", activebackground="darkgreen",
                           font=("Courier", 24), command=lambda: self.entr(entry))
        button.pack(pady=5)

        button = tk.Button(self, text="Назад на главную", bg="red", activebackground="darkred",
                           command=lambda: self.controller.show_frame(self.controller.home_frame),
                           font=("Courier", 24))
        button.pack(pady=5)

class Sign_up(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
    
    def add(self, var, entry):
        if (len(entry.get()) == 0):
            self.controller.show_mistake()
        else:
            if (var.get() == 0):
                with open('data_customers.txt', 'a') as keys:
                    keys.write(entry.get() + '\n')
            else:
                with open('data_sellers.txt', 'a') as keys:
                    keys.write(entry.get() + '\n')
            self.controller.show_success()

    def create_widgets(self):
        label = tk.Label(self, text="Регистрация", font=("Courier", 24))
        label.pack(pady=10)
        label = tk.Label(self, text="Введите свои данные", font=("Courier", 14))
        label.pack(pady=10)

        var = tk.IntVar()
        var.set(0)
        cust = tk.Radiobutton(self, text='покупатель', variable=var, value=0, font=("Courier", 14))
        cust.pack(pady=5)
        sell = tk.Radiobutton(self, text='продавец', variable=var, value=1, font=("Courier", 14))
        sell.pack(pady=5)

        entry = tk.Entry(self, width=25)
        entry.pack(pady=20)

        button = tk.Button(self, text="Зарегестрироваться", bg="green", activebackground="darkgreen",
                           font=("Courier", 20), command=lambda: self.add(var, entry))
        button.pack(pady=5)

        button = tk.Button(self, text="Назад на главную", bg="red", activebackground="darkred",
                           command=lambda: self.controller.show_frame(self.controller.home_frame),
                           font=("Courier", 20))
        button.pack(pady=20)

class Customer_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def Search(self, entry, tx):
        tx.delete(1.0, tk.END)
        if (len(entry.get()) == 0):
            self.controller.show_mistake()
        else:
            flag = 0
            i = 1.0
            with open('data_products.txt', 'r') as prod:
                lines = prod.readlines()
                for line in lines:
                    name = line[:line.find('*')]
                    price = line[line.find('*') + 1:]
                    if (entry.get() == name):
                        tx.insert(i, name + ' ' + price)
                        i += 1
                        flag = 1
                    line = prod.readline()
            if (flag == 0):
                self.controller.close_success()
                self.controller.show_mistake()
            else:
                self.controller.close_mistake()
                self.controller.show_success()
    
    def Buy(self, entry1, entry2, tx):
        if (len(entry1.get()) == 0 or len(entry2.get()) == 0):
            self.controller.show_mistake()
        else:
            flag = 0
            i = 0
            with open('data_products.txt', 'r') as prod:
                lines = prod.readlines()
                for line in lines:
                    name = line[:line.find('*')]
                    price = line[line.find('*') + 1:-1]
                    if (entry1.get() == name and entry2.get() == price):
                        flag = 1
                        break
                    line = prod.readline()
                    i += 1
            if (flag == 0):
                self.controller.close_success()
                self.controller.show_mistake()
            else:
                with open('data_products.txt', 'r') as prod:
                    lines = prod.readlines()
                lines.pop(i)
                with open('data_products.txt', 'w') as prod:
                    prod.writelines(lines)
                self.controller.close_mistake()
                self.controller.show_success()

    def create_widgets(self):
        label = tk.Label(self, text="Введите название товара", font=("Courier", 24))
        label.pack(pady=10)

        f1 = tk.Frame(self)
        f1.pack()

        tx = tk.Text(self, font=("Courier", 20), width=30, height=15)
        tx.pack(pady=10, padx=10)
        scroll = tk.Scrollbar(command=tx.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        tx.config(yscrollcommand=scroll.set)

        entry1 = tk.Entry(f1, width=20)
        entry1.pack(side=tk.LEFT, pady=10, padx=10)
        button = tk.Button(f1, text="Поиск", bg="green", activebackground="darkgreen",
                           command=lambda: self.Search(entry1, tx),
                           font=("Courier", 20))
        button.pack(side=tk.LEFT, pady=5, padx=5)

        label = tk.Label(self, text="Введите цену товара", font=("Courier", 24))
        label.pack(pady=10)
        entry2 = tk.Entry(self, width=20)
        entry2.pack(pady=10)
        button = tk.Button(self, text="Купить", bg="green", activebackground="darkgreen",
                           command=lambda: self.Buy(entry1, entry2, tx),
                           font=("Courier", 20))
        button.pack(pady=5)

        button = tk.Button(self, text="Назад на главную", bg="red", activebackground="darkred",
                           command=lambda: self.controller.show_frame(self.controller.home_frame),
                           font=("Courier", 20))
        button.pack(pady=5)

class Seller_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def add_product(self, name, price):
        with open('data_products.txt', 'a') as prod:
            if (len(name.get()) == 0 or len(price.get()) == 0):
                self.controller.show_mistake()
            else:
                prod.write(name.get() + '*' + price.get() + '\n')
                self.controller.close_mistake()
    
    def create_widgets(self):
        f1 = tk.Frame(self)
        f2 = tk.Frame(self)
        f3 = tk.Frame(self)
        f4 = tk.Frame(self)
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()

        label = tk.Label(f1, text="Добавьте товар", font=("Courier", 24))
        label.pack(pady=10)

        entry1 = tk.Entry(f2, width=20)
        entry1.pack(side=tk.LEFT, pady=10, padx=10)
        entry2 = tk.Entry(f3, width=20)
        entry2.pack(side=tk.LEFT, pady=10, padx=10)

        label = tk.Label(f2, text="название", font=("Courier", 14))
        label.pack(side=tk.LEFT, pady=10, padx=10)
        label = tk.Label(f3, text="цена", font=("Courier", 14))
        label.pack(side=tk.LEFT, pady=10, padx=10)

        button = tk.Button(self, text="Добавить", bg="green", activebackground="darkgreen",
                           command=lambda: self.add_product(entry1, entry2),
                           font=("Courier", 20))
        button.pack(pady=5)

        button = tk.Button(self, text="Назад на главную", bg="red", activebackground="darkred",
                           command=lambda: self.controller.show_frame(self.controller.home_frame),
                           font=("Courier", 20))
        button.pack(pady=5)

class Mistake(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        label = tk.Label(self, text="ОШИБКА", font=("Courier", 24), fg="red")
        label.pack(pady=10)

class Success(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        label = tk.Label(self, text="УСПЕШНО", font=("Courier", 24), fg="green")
        label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiWindowApp(root)
    root.mainloop()