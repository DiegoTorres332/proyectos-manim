from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))

class MatrixVectorMultiplication(Scene):
    def construct(self):
        # Create the identity matrix
        I = Matrix([[1, 0], [0, 1]])
        I.move_to(ORIGIN)
        
        # Create the exponent
        exponent = MathTex("^{n}")
        exponent.next_to(I, UR, buff=0.2)
        
        # Create the vector
        vector = Matrix([[1], [1]])
        vector.next_to(I, RIGHT, buff=0.5)
        
        # Create the equal sign
        equal_sign = MathTex("=")
        equal_sign.next_to(vector, RIGHT, buff=0.5)
        
        # Create the resulting vector
        result = Matrix([[2], [3]])
        result.next_to(equal_sign, RIGHT, buff=0.5)
        
        # Group the elements for convenience
        equation = VGroup(I, exponent, vector, equal_sign, result)
        
        # Animation sequence
        self.play(Write(I))
        self.wait(1)
        self.play(Write(exponent))
        self.wait(1)
        self.play(Write(vector))
        self.wait(1)
        self.play(Write(equal_sign))
        self.wait(1)
        self.play(Write(result))
        self.wait(2)


class MatrixVectorColor(Scene):
    def construct(self):
        # Define the matrices and vectors
        matrix = Matrix([
            ["a", "b"],
            ["c", "d"]
        ])
        vector = Matrix([
            ["x"],
            ["y"]
        ])
        result = Matrix([
            ["ax + by"],
            ["cx + dy"]
        ])

        # Position them on screen
        matrix.move_to(LEFT * 3)
        vector.next_to(matrix, RIGHT, buff=0.5)
        result.next_to(vector, RIGHT, buff=0.5)

        # Create the multiplication sign and equal sign
        mul_sign = MathTex(" \times ")
        mul_sign.next_to(matrix, RIGHT, buff=0.1)
        eq_sign = MathTex("=")
        eq_sign.next_to(result, LEFT, buff=0.1)

        # Display the matrix, vector, and result
        self.play(Write(matrix))
        self.play(Write(mul_sign))
        self.play(Write(vector))
        self.play(Write(eq_sign))
        self.play(Write(result))

        # Animate multiplication
        self.play(TransformFromCopy(matrix, result, path_arc=PI / 4))
        self.wait(2)

        # Color transformation
        # Define elements to color
        c_element = matrix.get_elements()[2]  # "c"
        x_element = vector.get_elements()[0]  # "x"
        d_element = matrix.get_elements()[3]  # "d"
        y_element = vector.get_elements()[1]  # "y"
        result_element = result.get_elements()[1]  # "cx + dy"

        # Animate the color change
        self.play(
            c_element.animate.set_color(RED),
            x_element.animate.set_color(RED),
            run_time=1
        )
        self.wait(1)

        self.play(
            d_element.animate.set_color(BLUE),
            y_element.animate.set_color(BLUE),
            run_time=1
        )
        self.wait(1)

        self.play(
            result_element.animate.set_color(PURPLE),
            run_time=1
        )
        self.wait(2)

	