from manim import *

class LimitFinder(Scene):
    
    def construct(self):

        limit_1 = MathTex(r"\lim_{n \to \infty} \frac{F_{n+1}}{F_n}")

        limit_1.move_to(ORIGIN)

        # Write the limit expression
        self.play(Write(limit_1))
        self.wait(7)

        limit_2 = MathTex(r"\lim_{n \to \infty} \frac{\frac{1}{\sqrt{5}} \left(\varphi^{n+1} + \frac{1}{\varphi^{n+1}}\right)}{\frac{1}{\sqrt{5}} \left(\varphi^n + \frac{1}{\varphi^n}\right)}")

        self.play(Transform(limit_1,limit_2))
        self.wait(3)

        limit_3 = MathTex(r"\lim_{n \to \infty} \frac{\varphi^{n+1} + \frac{1}{\varphi^{n+1}}}{\varphi^n + \frac{1}{\varphi^n}}")

        self.play(Transform(limit_1, limit_3))
        self.wait(9)

        limit_4 = MathTex(r"\lim_{n \to \infty} \frac{\varphi^{n+1}} {\varphi^n}")

        self.play(Transform(limit_1, limit_4))
        self.wait(4)

        limit_5 = MathTex(r"\lim_{n \to \infty} \varphi")

        self.play(Transform(limit_1,limit_5))
        self.wait(5)

        final_limit = MathTex(r"\varphi")
        final_limit.set_color(YELLOW)

        self.play(Transform(limit_1, final_limit))
        self.wait(6)