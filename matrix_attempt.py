from manim import * 

class MatrixGeneration(Scene):

	def construct(self):
		
		A=Matrix([[1,1],[1,0]])
		v_0=Matrix([["F_2"],["F_1"]])
		v_1=Matrix([[1],[1]])

		A.next_to(v_0, LEFT, buff=0.5)
		self.play(Create(A))
		self.play(Create(v_0))
		self.play(Transform(v_0,v_1))
		self.wait()


class Diagonalization(Scene):
    def construct(self):
        # Create matrices
        A = Matrix([[1, 1], [1, 0]])
        normalD = Matrix([["\\lambda", 0], [0, "\\lambda"]])
        specialD = Matrix([["\\varphi_1", 0], [0, "\\varphi_2"]])
        P = Matrix([["\\varphi_1", "\\varphi_2"], [1, 1]])

        # Create matrix P inverse with label
        P_inv_explicit = Matrix([["\\varphi_1", "\\varphi_2"], [1, 1]])
        P_inv_label = MathTex("^{-1}")
        P_inv_label.move_to(P_inv_explicit.get_corner(UP + RIGHT) + UP * 0.2)  # Adjust this as needed
        
        P_inv_group = VGroup(P_inv_explicit, P_inv_label)

        # Adjust position and alignment
        P_inv_group.arrange(RIGHT, buff=0.1)

        # Position matrices and formula
        formula = MathTex("A = P D P^{-1} = ")
        formula.move_to(LEFT * 3)

        A.next_to(formula, RIGHT, buff=0.5)
        P.next_to(A, LEFT)
        P_inv_group.next_to(A, RIGHT)

        # Animate the scene
        self.play(Write(formula))
        self.wait(1)

        self.play(Create(A))
        self.wait(1)

        self.play(Transform(A, normalD))
        self.wait(1)
        
        self.play(Transform(A, specialD))
        self.wait(1)

        # Move A further right to make space for the final group
        A_shifted = A.copy().shift(RIGHT * 2)  # Adjust the shift distance as needed

        # Create and scale down the final group
        final_group = VGroup(P, specialD, P_inv_group).arrange(RIGHT, buff=0.5)
        final_group.move_to(A_shifted.get_center())
        final_group.scale(0.75)  # Scale down the final group by 75%

        # Transforming P^-1 into its true form
        final_matrix = Matrix([[1, "-\\varphi_2"], ["-1", "\\varphi_1"]])
        true_final_group = VGroup(P, specialD, final_matrix).arrange(RIGHT, buff=0.5)
        true_final_group.move_to(A_shifted.get_center())
        true_final_group.scale(0.75)

        # Create the fraction expression and position it
        fraction_expr = MathTex(r"\frac{1}{\sqrt{5}}")
        fraction_expr.next_to(true_final_group, RIGHT, buff=0.5)

        # Animate transformation to final group
        self.play(Transform(A, final_group))
        self.wait(1)
        
        # Animate transformation to true_final_group
        self.play(Transform(A, true_final_group))
        self.wait(1)

        # Add the fraction expression
        self.play(Write(fraction_expr))
        self.wait(2)

class ExplicitFormula(Scene):
    def construct(self):
        first_eq = MathTex("A = P D P^{-1}")
        first_eq.move_to(ORIGIN)

        second_eq = MathTex(r"(A)^{n-1} = (PDP^{-1})^{n-1}")
        second_eq.move_to(ORIGIN)

        second_eq_expansion = MathTex(r"A^{n-1} = (PDP^{-1})(PDP^{-1})...(PDP^{-1})")
        second_eq_expansion.move_to(ORIGIN)

        second_eq_fullexpansion = MathTex(r"A^{n-1} = PD(P^{-1}P)D(P^{-1}P)...(P^{-1}P)DP^{-1}")
        second_eq_fullexpansion.move_to(ORIGIN)

        second_eq_final = MathTex(r"A^{n-1} = PD^{n-1}P^{-1}")
        second_eq_final.move_to(ORIGIN)

        A = Matrix([[1, 1], [1, 0]])
        A.move_to(ORIGIN)

        exponent_1 = MathTex("^{n-1}")
        exponent_1.next_to(A, UR, buff=0.2)

        D = Matrix([["\\varphi_1", 0], [0, "\\varphi_2"]])
        D.move_to(ORIGIN)

        specialD = Matrix([["\\varphi_1^{n-1}", "0"], ["0", "\\varphi_2^{n-1}"]])

        exponent_2 = MathTex("^{n-1}")
        exponent_2.next_to(D, UR, buff=0.2)

        P = Matrix([["\\varphi_1", "\\varphi_2"], [1, 1]])
        P.next_to(D, LEFT, buff=0.5)

        P_inv = Matrix([[1, "-\\varphi_2"], ["-1", "\\varphi_1"]])
        P_inv.next_to(D, RIGHT, buff=0.5)

        coefficient = MathTex(r"\frac{1}{\sqrt{5}}")
        coefficient.next_to(P, LEFT, buff=0.5)

        self.play(Write(first_eq))
        self.wait(2)
        self.play(Transform(first_eq, second_eq))
        self.wait(4)
        self.play(Transform(first_eq, second_eq_expansion))
        self.wait(4)
        self.play(Transform(first_eq, second_eq_fullexpansion))
        self.wait(4)
        self.play(Transform(first_eq, second_eq_final))
        self.wait(3)
        self.play(FadeOut(first_eq))
        self.wait(1)

        basic_group = VGroup(A, exponent_1)

        initial_group = VGroup(coefficient, P, D, exponent_2, P_inv).arrange(RIGHT, buff=0.5)
        final_group = VGroup(coefficient, P, specialD, P_inv).arrange(RIGHT, buff=0.5)

        self.play(Write(basic_group))
        self.wait(3)
        self.play(Transform(basic_group, initial_group))
        self.wait(2)
        self.play(Transform(basic_group, final_group))
        self.wait(6)

        first_vector = Matrix([["F_2"], ["F_1"]])
        first_vector.next_to(P_inv, RIGHT, buff=0.5)

        equal_sign = MathTex("=")
        equal_sign.next_to(first_vector, RIGHT, buff=0.5)

        final_vector = Matrix([["F_{n+1}"], ["F_n"]])
        final_vector.next_to(equal_sign, RIGHT, buff=0.5)

        total_group_fake = VGroup(coefficient, P, specialD, P_inv, first_vector, equal_sign, final_vector).arrange(RIGHT, buff=0.5)
        total_group_fake.scale(0.75)

        self.play(Transform(basic_group, total_group_fake))
        self.wait(2)

        first_vector_true = Matrix([[1], [1]])
        first_vector_true.next_to(P_inv, RIGHT, buff=0.5)
        first_vector_true.scale(0.75)

        total_group_true = VGroup(coefficient, P, specialD, P_inv, first_vector_true, equal_sign, final_vector).arrange(RIGHT, buff=0.5)

        self.play(Transform(basic_group, total_group_true))
        self.wait(2)

        first_2 = Matrix([["\\varphi_1^{n}", "\\varphi_2^{n}"], ["\\varphi_1^{n-1}", "\\varphi_2^{n-1}"]])
        first_2.scale(0.75)

        last_2 = Matrix([[r"1 - \varphi_2"], [r"\varphi_1 - 1"]])
        last_2.scale(0.75)

        last_push_matrix = VGroup(coefficient, first_2, last_2, equal_sign, final_vector).arrange(RIGHT, buff=0.5)

        self.play(Transform(basic_group, last_push_matrix))
        self.wait(4)

        first_matrix = first_2.get_elements()[2]
        first_vector = last_2.get_elements()[0]
        second_matrix = first_2.get_elements()[3]
        second_vector = last_2.get_elements()[1]
        result_vector = final_vector.get_elements()[1]

        self.play(first_matrix.animate.set_color(RED), first_vector.animate.set_color(RED), run_time=1)
        self.wait(1)

        self.play(second_matrix.animate.set_color(BLUE), second_vector.animate.set_color(BLUE), run_time=1)
        self.wait(1)

        self.play(result_vector.animate.set_color(PURPLE), run_time=1)
        self.wait(3)

        self.play(FadeOut(basic_group),FadeOut(last_push_matrix))

        # new form
        coefficient_1 = MathTex(r"\frac{1}{\sqrt{5}}")
        parentheses_left = MathTex(r"(")
        term1 = MathTex(r"\varphi_1^{n-1} (1 - \varphi_2)")
        plus_sign = MathTex(r"+")
        term2 = MathTex(r"\varphi_2^{n-1} (\varphi_1 - 1)")
        parentheses_right = MathTex(r")")
        equalsign = MathTex(r"=")
        result = MathTex(r"F_n")

        coefficient_1.move_to(LEFT * 3)
        parentheses_left.next_to(coefficient, RIGHT, buff=0.5)
        term1.next_to(parentheses_left, RIGHT, buff=0.5)
        term2.next_to(term1, RIGHT, buff=0.5)
        parentheses_right.next_to(term2, RIGHT, buff=0.5)
        plus_sign.next_to(parentheses_right, RIGHT, buff=0.5)
        equalsign.next_to(plus_sign, RIGHT, buff=0.5)
        result.next_to(equalsign, RIGHT, buff=0.5)

        # Color each term
        term1.set_color(RED)
        term2.set_color(BLUE)
        result.set_color(PURPLE)

        # Combine terms into a VGroup
        equation_group = VGroup(coefficient_1, parentheses_left, term1, plus_sign, term2, parentheses_right, equalsign, result).arrange(RIGHT, buff=0.5)

        self.play(Write(equation_group))
        self.wait(5)

        term_1_bad = MathTex(r"(\varphi^{n-1})\left(1 - \left(-\frac{1}{\varphi}\right)\right)")
        term_2_bad = MathTex(r"(\frac{1}{\varphi^{n-1}})(\varphi - 1)")

        new_equation_group = VGroup(coefficient_1, parentheses_left, term_1_bad, plus_sign, term_2_bad, parentheses_right, equalsign, result).arrange(RIGHT, buff=0.5)

        self.play(Transform(equation_group,new_equation_group))
        self.wait(5)

        term_1 = MathTex(r"(\varphi^{n-1})\left(1 + \left(\frac{1}{\varphi}\right)\right)")
        term_2 = MathTex(r"(\frac{1}{\varphi^{n-1}})(\varphi - 1)")

        super_new_equation_group = VGroup(coefficient_1, parentheses_left, term_1, plus_sign, term_2, parentheses_right, equalsign, result).arrange(RIGHT, buff=0.5)

        self.play(Transform(equation_group, super_new_equation_group))
        self.wait(5)

        last_term_1 = MathTex(r"(\varphi^{n-1})(\varphi)")
        last_term_2 = MathTex(r"(\frac{1}{\varphi^{n-1}})(-\frac{1}{\varphi})")

        hyper_new_equation_group = VGroup(coefficient_1, parentheses_left, last_term_1, plus_sign, last_term_2, parentheses_right, equalsign, result).arrange(RIGHT, buff=0.5)

        self.play(Transform(equation_group, hyper_new_equation_group))
        self.wait(5)

        final_term_1 = MathTex(r"\varphi^n")
        final_term_2 = MathTex(r"\frac{1}{\varphi^n}")

        ultimate_new_equation_group = VGroup(coefficient_1, parentheses_left, final_term_1, plus_sign, final_term_2, parentheses_right, equalsign, result).arrange(RIGHT, buff=0.5)
        
        self.play(Transform(equation_group, ultimate_new_equation_group))
        self.wait(6)
