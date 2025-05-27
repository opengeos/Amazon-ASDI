import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## Amazon Sustainability Data Initiative (ASDI)

        An Interactive Web App for Visualizing Open Data from the Amazon Sustainability Data Initiative ([ASDI](https://exchange.aboutamazon.com/data-initiative)).
        Click on the menu above to explore the data.

        ![image](https://github.com/user-attachments/assets/8f7a18cd-bfe8-444a-add4-2d21a1830053)
        """

        solara.Markdown(markdown)
