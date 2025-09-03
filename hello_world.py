class HelloWorld:
    def print_with_border(self, text: str, border_char: str = "*"):
        padding = 4
        inner_width = len(text) + padding
        top_bottom = border_char * (inner_width + 6)

        print(top_bottom)
        print(f"{border_char*2}{' ' * (inner_width + 2)}{border_char*2}")
        print(f"{border_char*2} {text.center(inner_width)} {border_char*2}")
        print(f"{border_char*2}{' ' * (inner_width + 2)}{border_char*2}")
        print(top_bottom)
        
if __name__ == "__main__":
    hw = HelloWorld()
    hw.print_with_border("Hello World", "=")