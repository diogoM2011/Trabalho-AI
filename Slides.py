from manim import *
from manim_slides import Slide

class ApresentacaoEminem(Slide):
    def construct(self):
        # Configuração inicial de cores (Fundo claro para destacar texto escuro)
        self.camera.background_color = "#F4F4F4"
        cor_titulo = "#1A1A1A"
        cor_texto = "#333333"
        cor_destaque = "#B22222" # Vermelho escuro para destacar elementos

        # =========================================================================
        # SLIDE 1: Introdução e Identidade
        # =========================================================================
        t1 = Text("Marshall Bruce Mathers III", color=cor_titulo, font_size=40).shift(UP * 2)
        sub1 = Text("Eminem: A Personalidade", color=cor_destaque, font_size=28).next_to(t1, DOWN, buff=0.3)
        
        # Detalhes rápidos em formato de lista (VGroup para organizar)
        detalhes1 = VGroup(
            Text("- Nascimento: 17/10/1972 (53 anos)", color=cor_texto, font_size=22),
            Text("- Álbum de Estreia: 'The Slim Shady LP' (1999)", color=cor_texto, font_size=22),
            Text("- Ícones: 'Without Me', 'Mockingbird', 'Rap God'", color=cor_texto, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(t1), FadeIn(sub1))
        self.play(FadeIn(detalhes1, shift=UP))
        self.next_slide() # Pausa o slide para a vossa explicação

        # Limpeza para o próximo slide
        self.play(FadeOut(t1), FadeOut(sub1), FadeOut(detalhes1))


        # =========================================================================
        # SLIDE 2: As Três Personagens (A Mente)
        # =========================================================================
        t2 = Text("A Mente Dividida", color=cor_titulo, font_size=36).shift(UP * 2.5)
        self.play(Write(t2))

        # Criar 3 caixas textuais para as 3 personas
        p_marshall = VGroup(
            Text("Marshall Mathers", color=cor_destaque, font_size=24, weight=BOLD),
            Text("O lado humano e instável.\nInfância traumática,\namor pelas 3 filhas.", color=cor_texto, font_size=18, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT * 4.5 + UP * 0.5)

        p_eminem = VGroup(
            Text("Eminem", color=cor_destaque, font_size=24, weight=BOLD),
            Text("O artista focado.\nObcecado pelo trabalho e\nperfeição técnica.", color=cor_texto, font_size=18, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 0.5)

        p_slim = VGroup(
            Text("Slim Shady", color=cor_destaque, font_size=24, weight=BOLD),
            Text("O alter ego sombrio.\nSarcástico, rebelde,\nraiva e humor negro.", color=cor_texto, font_size=18, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 4.5 + UP * 0.5)

        self.play(FadeIn(p_marshall, shift=RIGHT))
        self.play(FadeIn(p_eminem, shift=UP))
        self.play(FadeIn(p_slim, shift=LEFT))
        self.next_slide()

        self.play(FadeOut(t2), FadeOut(p_marshall), FadeOut(p_eminem), FadeOut(p_slim))


        # =========================================================================
        # SLIDE 3: O Caminho e as Barreiras (Origens)
        # =========================================================================
        t3 = Text("Origens e Superação", color=cor_titulo, font_size=36).shift(UP * 2.5)
        
        barreiras = VGroup(
            Text("• Pobreza e Bullying: Abandono escolar e coma de 10 dias.", color=cor_texto, font_size=22),
            Text("• Preconceito Racial: Jovem branco num género predominantemente negro.", color=cor_texto, font_size=22),
            Text("• Dependência Química: Auge em 1999 (20 comprimidos/dia).", color=cor_texto, font_size=22),
            Text("• Sobriedade: Processo iniciado em 2007; total em Abril de 2008.", color=cor_destaque, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.2)

        self.play(Write(t3))
        self.play(FadeIn(barreiras, shift=UP))
        self.next_slide()

        self.play(FadeOut(t3), FadeOut(barreiras))


        # =========================================================================
        # SLIDE 4: Impacto na Cultura e Estilo Técnico
        # =========================================================================
        t4 = Text("Cultura e Inovação Técnica", color=cor_titulo, font_size=36).shift(UP * 2.5)
        
        cultura_info = VGroup(
            Text("• Velocidade e Métrica: 'Rap God' com 1.560 palavras em 6 minutos.", color=cor_texto, font_size=22),
            Text("• Crítica ao Sistema: 'White America' expõe o privilégio e racismo comercial.", color=cor_texto, font_size=22),
            Text("• Quebra de Barreiras: Ganhou respeito mundial através de batalhas de rap.", color=cor_texto, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.2)

        self.play(Write(t4))
        self.play(FadeIn(cultura_info, shift=RIGHT))
        self.next_slide()

        self.play(FadeOut(t4), FadeOut(cultura_info))


        # =========================================================================
        # SLIDE 5: Comunidade e Causas Sociais
        # =========================================================================
        t5 = Text("Intervenção na Comunidade", color=cor_titulo, font_size=36).shift(UP * 2.5)
        
        causas = VGroup(
            Text("• Crítica Política: Uso do Slim Shady contra George W. Bush.", color=cor_texto, font_size=22),
            Text("• Apoio a Jovens em Risco: Financiamento de escolas e centros juvenis.", color=cor_texto, font_size=22),
            Text("• Combate à Fome Escolar: Doação de +700 mil dólares para almoços.", color=cor_texto, font_size=22),
            Text("• Apoio aos Sem-Abrigo: Milhões investidos em alojamentos de emergência.", color=cor_texto, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(DOWN * 0.2)

        self.play(Write(t5))
        self.play(FadeIn(causas, shift=LEFT))
        self.next_slide()

        self.play(FadeOut(t5), FadeOut(causas))


        # =========================================================================
        # SLIDE 6: Legado e Conclusão
        # =========================================================================
        t6 = Text("O Legado de Marshall Mathers", color=cor_titulo, font_size=36).shift(UP * 2.5)
        
        conclusao = VGroup(
            Text("• Humanização do Rap: Introduziu ansiedade, depressão e fraquezas no género.", color=cor_texto, font_size=22),
            Text("• Termo 'Stan': Entrou oficialmente no dicionário de Oxford (fã obsessivo).", color=cor_texto, font_size=22),
            Text("• Mensagem Principal: Nunca desistir dos sonhos perante as contrariedades.", color=cor_destaque, font_size=22),
            Text("• Descoberta: Visto pelo Dr. Dre em 1997 num estúdio caseiro.", color=cor_texto, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.2)

        self.play(Write(t6))
        self.play(FadeIn(conclusao, shift=UP))
        self.next_slide()

        # Encerramento
        fim = Text("Obrigado pela vossa atenção!", color=cor_destaque, font_size=32).shift(DOWN * 2.5)
        self.play(FadeIn(fim))
        self.next_slide()
