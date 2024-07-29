"""Part-to-whole charts."""

import vizro.models as vm
import vizro.plotly.express as px

from pages._pages_utils import PAGE_GRID, gapminder_2007, make_code_clipboard_from_py_file, tips

pie = vm.Page(
    title="Pie",
    path="part-to-whole/pie",
    layout=vm.Layout(grid=PAGE_GRID),
    components=[
        vm.Card(
            text="""

            #### What is a pie chart?

            A pie chart is a circular chart divided into segments to show proportions and percentages between
            categories. The circle represents the whole.

            &nbsp;

            #### When should I use it?

            Use the pie chart when you need to show your audience a quick view of how data is distributed
            proportionately, with percentages highlighted. The different values you present must add up to a total and
            equal 100%.

            The downsides are that pie charts tend to occupy more space than other charts, they don't
            work well with more than a few values because labeling small segments is challenging, and it can be
            difficult to accurately compare the sizes of the segments.
        """
        ),
        vm.Graph(
            figure=px.pie(
                tips,
                values="tip",
                names="day",
            )
        ),
        make_code_clipboard_from_py_file("pie.py"),
    ],
)

donut = vm.Page(
    title="Donut",
    path="part-to-whole/donut",
    layout=vm.Layout(grid=PAGE_GRID),
    components=[
        vm.Card(
            text="""

            #### What is a donut chart?

            A donut chart looks like a pie chart, but has a blank space in the center which may contain additional
            information.

            &nbsp;

            #### When should I use it?

            A donut chart can be used in place of a pie chart, particularly when you are short of space or have extra
            information you would like to share about the data. It may also be more effective if you wish your audience
            to focus on the length of the arcs of the sections instead of the proportions of the segment sizes.
        """
        ),
        vm.Graph(
            figure=px.pie(
                tips,
                values="tip",
                names="day",
                hole=0.4,
            )
        ),
        make_code_clipboard_from_py_file("pie.py"),
    ],
)

treemap = vm.Page(
    title="Treemap",
    path="part-to-whole/treemap",
    layout=vm.Layout(grid=PAGE_GRID),
    components=[
        vm.Card(
            text="""

                #### What is a treemap?

                A treemap shows hierarchical data arranged as a set of nested rectangles: rectangles are sized
                proportionately to the quantity they represent, combined together to form larger parent category
                rectangles.

                &nbsp;

                #### When should I use it?

                It's helpful to use a treemap when you wish to display hierarchical part-to-whole relationships. You can
                compare groups and single elements nested within them. Consider using them instead of Pie charts when
                you have a higher number of categories. Treemaps are very compact and allow audiences to get a quick
                overview of the data.
            """
        ),
        vm.Graph(
            figure=px.treemap(
                gapminder_2007,
                path=[px.Constant("world"), "continent", "country"],
                values="pop",
                color="lifeExp",
            )
        ),
        make_code_clipboard_from_py_file("treemap.py"),
    ],
)

pages = [donut, pie, treemap]
