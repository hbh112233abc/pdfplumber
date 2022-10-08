# pdfplumber

[![Version](https://img.shields.io/pypi/v/pdfplumber.svg)](https://pypi.python.org/pypi/pdfplumber) ![Tests](https://github.com/jsvine/pdfplumber/workflows/Tests/badge.svg) [![Code coverage](https://codecov.io/gh/jsvine/pdfplumber/branch/stable/graph/badge.svg)](https://codecov.io/gh/jsvine/pdfplumber/branch/stable) [![Support Python versions](https://img.shields.io/pypi/pyversions/pdfplumber.svg)](https://pypi.python.org/pypi/pdfplumber)

解析PDF文件,获取相关的文本字符、矩形和线条的详细信息。 额外功能：表格提取和可视化调试。

用于电脑生成的PDF上效果最好，不支持扫描的PDF，基于[`pdfminer.six`](https://github.com/goulu/pdfminer)实现.

当前版本 [测试用例](tests/) 已经在 [Python 3.7, 3.8, 3.9, 3.10](.github/workflows/tests.yml) 验证通过.

**反馈BUG** 或提交功能, 请 [提交issue](https://github.com/jsvine/pdfplumber/issues/new/choose). **有疑问** 或提交需要协助的特殊PDF文件, 请 [进入讨论区](https://github.com/jsvine/pdfplumber/discussions).

> 👋 本项目维护人员提供PDF数据提取服务. 询价可联系 [Jeremy](https://www.jsvine.com/consulting/pdf-data-extraction/) (针对任何项目) 或 [Samkit](https://www.linkedin.com/in/samkit-jain/) (针对表格提取).

## 目录

*   [安装](#installation)

*   [命令行](#command-line-interface)

*   [Python包](#python-library)

*   [可视化调试](#visual-debugging)

*   [提取表格](#extracting-tables)

*   [提取表单域值](#extracting-form-values)

*   [用例演示](#demonstrations)

*   [与其他库比较](#comparison-to-other-libraries)

*   [认可及贡献](#acknowledgments--contributors)

*   [贡献代码](#contributing)

## 安装

```sh
pip install pdfplumber
```

## 命令行

### 基础示例

```sh
curl "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf" > background-checks.pdf
pdfplumber < background-checks.pdf > background-checks.csv
```

输出将是一个CSV，包含PDF中每个字符、行和矩形的信息。

### 配置项

| 参数                   | 说明                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `--format [输出格式]`    | `csv` 或 `json`. `json` 返回信息包括PDF文件级和页面级元数据，以及字典嵌套属性。                                        |
| `--pages [页码]`       | `1`-页面索引或页面范围. 举例: `1, 11-15`, 指定的页面范围: 1, 11, 12, 13, 14, 15.                              |
| `--types [提取对象类型列表]` | 可选值: `char`, `rect`, `line`, `curve`, `image`, `annot`等,默认全部提取                              |
| `--laparams`         | json格式字符串 (例: `'{"detect_vertical": true}'`) PDF打开的传参 `pdfplumber.open(..., laparams=...)`. |
| `--precision [整数]`   | 浮点数四舍五入的小数位数。默认为无舍入。                                                                        |

## Python库

### 基础示例

```python
import pdfplumber

with pdfplumber.open("path/to/file.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
```

### 加载PDF

调用`pdfplumber.open(x)`加载PDF, 其中`x`可以有以下几种格式:

*   PDF文件路径

*   文件对象, 以字节流形式加载

*   类文件对象, 以字节流形式加载

`open`方法加载文件后返回一个 `pdfplumber.PDF` 实例.

传入 `password` 参数用于加载已加密的PDF文件, 例: `pdfplumber.open("file.pdf", password = "test")`.

传入 `laparams` 参数可以使用`pdfminer.six`的布局引擎用于布局分析, 例: `pdfplumber.open("file.pdf", laparams = { "line_overlap": 0.7 })`.

Invalid metadata values are treated as a warning by default. If that is not intended, pass `strict_metadata=True` to the `open` method and `pdfplumber.open` will raise an exception if it is unable to parse the metadata.

默认情况下，无效元数据值只是被视为警告。如果设置`strict_metadata=True`。当加载PDF后无法分析元数据，将抛出异常。

### `pdfplumber.PDF` 类

`pdfplumber.PDF` 类代表一个PDF文件,主要有以下两个属性:

| 属性          | 说明                                                                              |
| ----------- | ------------------------------------------------------------------------------- |
| `.metadata` | 元数据键/值对字典，摘自PDF的“信息”。通常包括“CreationDate”(创建日期)、“ModDate”(修改日期)、“Producer”(创建者)等。 |
| `.pages`    | 包含`pdfplumber.Page`(页实例)的列表。                                                    |

### `pdfplumber.Page` 类

`pdfplumber.Page`是`pdfplumber`核心. 大部分的操作都是围绕此类进行.主要包含以下属性:

| 属性                                                                  | 说明                                                                          |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `.page_number`                                                      | 页码, `1`第一页, `2`第二页, 以此类推.                                                   |
| `.width`                                                            | 页面宽.                                                                        |
| `.height`                                                           | 页面高.                                                                        |
| `.objects` / `.chars` / `.lines` / `.rects` / `.curves` / `.images` | 这些属性中的每一个都是一个列表，每个列表都为嵌入在页面上的每个此类对象包含一个字典。有关详细信息，请参见 "[Objects](#objects)". |

... `pdfplumber.Page`的主要方法:

| 方法                                                                                                                                                  | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.crop(bounding_box, relative=False, strict=True)`                                                                                                               | 返回裁剪边界框中的页面内容，边界框应表示为4元组，值为 `(x0, top, x1, bottom)`。裁剪的页面保留至少部分位于边界框内的对象。如果对象仅部分落在长方体中，则将剖切其被边界框包含的部分。如果`relative=True`，则边界框计算为距页面左上角的偏移量，而不是绝对位置。 (参考 [Issue #245](https://github.com/jsvine/pdfplumber/issues/245) 给出的直观示例和说明.) 当`strict=True` (默认值), 裁剪框必须在页面边界内部.                                                                                                                                                                                                                                                                                                                                      |
| `.within_bbox(bounding_box, relative=False, strict=True)`                                                                                                        | 类似`.crop`,但仅保留完全落在边界框内的对象。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|`.outside_bbox(bounding_box, relative=False, strict=True)`| 类似`.crop` 和 `.within_bbox`, 仅保留边界框外部的对象.|
| `.filter(test_function)`                                                                                                                            | 过滤对象`.objects`,仅提取当过滤函数`test_function(obj)`返回`True`的对象.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `.dedupe_chars(tolerance=1)`                                                                                                                        | 删除重复的字符-与其他字符共享相同的文本、字体名称、大小和位置（在“公差”x/y范围内）-已删除. (参考 [Issue #71](https://github.com/jsvine/pdfplumber/issues/71)了解该机制)                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `.extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13, **kwargs)`                                                 | 将页面的所有字符对象整理为单个字符串.`layout=False`: 当字符`x1`(右x坐标)下一个字符`x0`(左x坐标)的公差大于`x_tolerance`时添加空格. 当字符`doctop`(上y坐标)与下一个字符`doctop`(上y坐标) 公差大于 `y_tolerance`时添加换行.设置 `layout=True` (*实验特性*): 尝试模拟页面上的文本结构布局, 使用 `x_density` 和 `y_density` 确定每个“点”的最小字符/换行数，即PDF度量单位.其他传参`**kwargs` 参考`.extract_words(...)`传参.                                                                                                                                                                                                                                                                      |
| `.extract_words(x_tolerance=3, y_tolerance=3, keep_blank_chars=False, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[], split_at_punctuation=False)`| 返回词块的内容及边框. 如果（“垂直”字符）一个字符的`x1`与下一个字符的`x0`之间的差值小于或等于`x_tolerance` 并且 一个字符的 `doctop`与下一个字符的 `doctop`小于或等于 `y_tolerance`，则单词被视为字符序列.对于非垂直字符，也采用类似的方法，但测量它们之间的垂直距离，而不是水平距离。参数 `horizontal_ltr` 和 `vertical_ttb` 表示阅读顺序为水平由左至右的顺序及垂直由上而下的顺序. 设置 `keep_blank_chars`为 `True`将空格作为单词的一部分而不是分隔符. 设置 `use_text_flow` 为 `True`将使用PDF的基本字符流作为单词排序和分段的指南，而不是按x/y位置对字符进行预排序。 (这模仿了拖动光标如何突出显示PDF中的文本；因此，顺序并不总是符合逻辑的。) 设置`extra_attrs`额外属性列表  (例: `["fontname", "size"]` 将每个单词限制为每个单词共享完全相同值的字符 [字符属性](https://github.com/jsvine/pdfplumber/blob/develop/README.md#char-属性), 查看单词属性字典; 将`split_at_spurtation`设置为`True`将在`string.punctuation`标点处强制中断；或者您也可以通过传递字符串来指定分隔标点符号的列表，例如: <code>split_at_spursion='！“&\'（）*+，.：；<=>？@[\]^\`\{|\}~'</code>|
| `.search(pattern, regex=True, case=True, **kwargs)`                                                                                                 | *实验特性* 它允许您搜索页面的文本，返回与查询匹配的所有实例的列表。对于每个实例，返回对象都包含匹配的文本、任何正则表达式组匹配项、边界框坐标以及char对象本身 `pattern`可以是已编译的正则表达式、未编译的正则表达式或非正则表达式字符串。如果`regex`为 `False`，则该模式将被视为非regex字符串。如果 `case`为`False`，则以不区分大小写的方式执行搜索。 其他参数 `**kwargs` 参考 `.extract_text(layout=True, ...)`.                                                                                                                                                                                                                                                                                                             |
| `.extract_tables(table_settings)`                                                                                                                   | 提取页面表格数据. 详情参考 "[Extracting tables](#extracting-tables)".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `.to_image(**conversion_kwargs)`                                                                                                                    | 返回 `PageImage` 实例. 详情参见 "[可视化调试](#visual-debugging)" . 转换参数参见 [here](http://docs.wand-py.org/en/latest/wand/image.html#wand.image.Image).                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `.close()`                                                                                                                                          | 默认`Page` 对象会缓存其布局和对象信息，以避免重新处理。然而，在解析大型PDF时，这些缓存属性可能需要大量内存。可以使用此方法刷新缓存并释放内存 (旧版本 `<= 0.5.25`, 请使用 `.flush_cache()`.)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### 对象

`pdfplumber.PDF` 和 `pdfplumber.Page`实例均提供各种类型的对象, 对象来自 [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six/)PDF解析。以下属性分别返回匹配对象的Python列表：

*   `.chars`, 代表单个文本字符.

*   `.lines`, 代表一条一维线.

*   `.rects`, 代表单个二维矩形.

*   `.curves`, 代表一序列`pdfminer.six`无法识别成线或矩形的连接点,.

*   `.images`, 代表图像.

*   `.annots`, 代表一个PDF批注 (详见第8.4节 [官方PDF规范](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/pdf_reference_1-7.pdf))

*   `.hyperlinks`, 代表链接注释 `Link`包含`URI`属性

以上每个对象都是字典形式,其包含以下属性:

#### `char` 属性

| 属性                   | 说明                             |
| -------------------- | ------------------------------ |
| `page_number`        | 找到此字符的页码。                      |
| `text`               | 文本内容 例: "z", 或 "Z" 或 " ".      |
| `fontname`           | 字体                             |
| `size`               | 字号                             |
| `adv`                | 等于文本宽度*字体大小*比例因子。              |
| `upright`            | 是否垂直                           |
| `height`             | 文本高度                           |
| `width`              | 文本高度                           |
| `x0`                 | 其左侧与页面左侧的距离。                   |
| `x1`                 | 其右侧与页面左侧的距离。                   |
| `y0`                 | 其下侧与页面底部的距离。                   |
| `y1`                 | 其上侧与页面底部的距离。                   |
| `top`                | 其上侧与页面顶部的距离。                   |
| `bottom`             | 其下侧与页面顶部的距离。                   |
| `doctop`             | 其顶部与文档顶部的距离。                   |
| `matrix`             | 其“变换矩阵”。（详见下文）                 |
| `stroking_color`     | 笔划的颜色，表示为元组或整数，具体取决于使用的“颜色空间”。 |
| `non_stroking_color` | 字体填充颜色                         |
| `object_type`        | 对象类型:"char"                    |

**备注**: 文本变换矩阵(`matrix`)说明请参见章节4.2.2[PDF参考](https://ghostscript.com/\~robin/pdf_reference17.pdf) (第6版). 矩阵控制角色的缩放、倾斜和位置平移。旋转是缩放和倾斜的组合，但在大多数情况下可以认为等于x轴倾斜。 `pdfplumber.ctm`子模块定义了一个类 `CTM`，该类可以帮助进行这些计算。例如：

```python
from pdfplumber.ctm import CTM
my_char = pdf.pages[0].chars[3]
my_char_ctm = CTM(*my_char["matrix"])
my_char_rotation = my_char_ctm.skew_x
```

#### `line` 属性

| 属性                   | 说明                           |
| -------------------- | ---------------------------- |
| `page_number`        | 其所在的页码                       |
| `height`             | 高度                           |
| `width`              | 宽度                           |
| `x0`                 | 其左侧与页面左侧的距离。                 |
| `x1`                 | 其右侧与页面左侧的距离。                 |
| `y0`                 | 其下侧与页面底部的距离。                 |
| `y1`                 | 其上侧与页面底部的距离。                 |
| `top`                | 其上侧与页面顶部的距离。                 |
| `bottom`             | 其下侧与页面顶部的距离。                 |
| `doctop`             | 其顶部与文档顶部的距离。                 |
| `linewidth`          | 线粗                           |
| `stroking_color`     | 线条颜色,表示为元组或整数，具体取决于使用的“颜色空间” |
| `non_stroking_color` | 线条填充颜色。                      |
| `object_type`        | 对象类型:"line"                  |

#### `rect` 属性

| 属性                   | 说明                           |
| -------------------- | ---------------------------- |
| `page_number`        | 其所在的页码                       |
| `height`             | 高度                           |
| `width`              | 宽度                           |
| `x0`                 | 其左侧与页面左侧的距离。                 |
| `x1`                 | 其右侧与页面左侧的距离。                 |
| `y0`                 | 其下侧与页面底部的距离。                 |
| `y1`                 | 其上侧与页面底部的距离。                 |
| `top`                | 其上侧与页面顶部的距离。                 |
| `bottom`             | 其下侧与页面顶部的距离。                 |
| `doctop`             | 其顶部与文档顶部的距离。                 |
| `linewidth`          | 线粗                           |
| `stroking_color`     | 线条颜色,表示为元组或整数，具体取决于使用的“颜色空间” |
| `non_stroking_color` | 线条填充颜色。                      |
| `object_type`        | 对象类型:"rect"                  |

#### `curve` 属性

| 属性                   | 说明                                |
| -------------------- | --------------------------------- |
| `page_number`        | 其所在的页码                            |
| `points`             | Points — 描述曲线的点列表包含 `(x, top)` 元组 |
| `height`             | 曲线边界框的高度。                         |
| `width`              | 曲线边界框的宽度。                         |
| `x0`                 | 曲线最左侧点与页面左侧的距离。                   |
| `x1`                 | 曲线最右侧点与页面左侧的距离。                   |
| `y0`                 | 曲线最低点到页面底部的距离。                    |
| `y1`                 | 曲线最高点到页面底部的距离。                    |
| `top`                | 曲线最高点到页面顶部的距离。                    |
| `bottom`             | 曲线最低点到页面底部的距离。                    |
| `doctop`             | 曲线最高点到文档顶部的距离。                    |
| `linewidth`          | 线粗                                |
| `fill`               | 是否填充曲线路径定义的形状.                    |
| `stroking_color`     | 曲线轮廓的颜色，表示为元组或整数，具体取决于使用的“颜色空间”。  |
| `non_stroking_color` | 曲线填充颜色                            |
| `object_type`        | 对象类型:"curve"                      |

此外， `pdfplumber.PDF` 和 `pdfplumber.Page`还提供以下两个对象：
`.rect_edges` （将每个矩形分解为四条线）
`.edges`（将 `.rect_edges`与 `.lines`组合在一起）。

#### `image` 属性

\[待完善.]

### 获取`pdfminer.six`高级布局对象

加载PDF( `pdfplumber.open(...)`)时通过传参`laparams`打开PDF后,每个页面对象将包含 `pdfminer.six`高级布局对象, 例如: `"textboxhorizontal"`.

## 可视化调试

**备注:** 使用`pdfplumber`的可视化调试工具, 需要先安装以下两个软件:

*   [`ImageMagick`](https://www.imagemagick.org/). [Installation instructions here](http://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-debian).

*   [`ghostscript`](https://www.ghostscript.com). [Installation instructions here](https://www.ghostscript.com/doc/current/Install.htm),或者 `apt install ghostscript` (Ubuntu) / `brew install ghostscript` (Mac).

### 输出页面图像对象 `PageImage`

使用 `my_page.to_image()`获取页面(包括裁剪页面)的图像对象 `PageImage` .设置分辨率`resolution={integer}`, 默认分辨率:72 例:

```python
im = my_pdf.pages[0].to_image(resolution=150)
```

使用脚本或交互环境时,`im.show()`将使用本地图片浏览器查看图片, `PageImage` 对象也可以很好地与IPython/Jupyter笔记本电脑配合使用；它们会自动渲染为单元格输出。例如：

![使用Jupyter进行可视化调试](examples/screenshots/visual-debugging-in-jupyter.png "Visual debugging in Jupyter")

### `PageImage` 基础方法

| 方法                                          | 说明                     |
| ------------------------------------------- | ---------------------- |
| `im.reset()`                                | 重置,清除已绘制的所有内容。         |
| `im.copy()`                                 | 将图像复制到新的“PageImage”对象。 |
| `im.show()`                                 | 使用本地图片查看器浏览图片|
| `im.save(path_or_fileobject, format="PNG")` | 保存已标记的图片               |

### 绘制方法

你可以传递坐标或`pdfplumber`PDF对象 (例: char, line, rect)进行绘图.

| 单对象绘制                                                                     | 批量绘制                                          | 说明                                                      |
| ------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------- |
| `im.draw_line(line, stroke={color}, stroke_width=1)`                      | `im.draw_lines(list_of_lines, **kwargs)`      | 绘制线条根据`line`, `curve`, 或起止点坐标元组(例: `((x, y), (x, y))`). |
| `im.draw_vline(location, stroke={color}, stroke_width=1)`                 | `im.draw_vlines(list_of_locations, **kwargs)` | 在`location`处x坐标处绘制一条垂直线                                 |
| `im.draw_hline(location, stroke={color}, stroke_width=1)`                 | `im.draw_hlines(list_of_locations, **kwargs)` | 在`location`处y坐标处绘制一条水平线                                 |
| `im.draw_rect(bbox_or_obj, fill={color}, stroke={color}, stroke_width=1)` | `im.draw_rects(list_of_rects, **kwargs)`      | 绘制矩形`rect`, `char`, 等, 或4坐标元组边界框.                       |
| `im.draw_circle(center_or_obj, radius=5, fill={color}, stroke={color})`   | `im.draw_circles(list_of_circles, **kwargs)`  | 以`(x, y)`为圆心画圆 `char`, `rect`, 等.                       |

备注:以上绘图方法是基于Pillow实现的 [`ImageDraw` methods](http://pillow.readthedocs.io/en/latest/reference/ImageDraw.html), 但是为了与SVG的一致性，调整了`fill`/`stroke`/`stroke_width`参数命名.

### Debian系统修复ImageMagick问题

如果你在Debian系统使用`pdfplumber`遇到了`PolicyError`错误,你需要修改 `/etc/ImageMagick-6/policy.xml`:

```xml
<policy domain="coder" rights="none" pattern="PDF" />
```

修改为:

```xml
<policy domain="coder" rights="read|write" pattern="PDF" />
```

(`policy.xml`[详细说明](https://imagemagick.org/script/security-policy.php).)

## 提取表格

`pdfplumber`提取表格大部分借鉴 [Anssi Nurminen的硕士论文](http://dspace.cc.tut.fi/dpub/bitstream/handle/123456789/21520/Nurminen.pdf?sequence=3), 灵感来源于 [Tabula](https://github.com/tabulapdf/tabula-extractor/issues/16). 工作流程如下:

1.  针对PDF页面, 查找（a）明确定义的行和/或（b）页面上单词对齐所隐含的行。

2.  合并重叠或接近重叠的线条.

3.  找出这些线条的交点.

4.  找到使用这些交点作为顶点的最细粒度的矩形集（即单元格）。

5.  将连续单元格分组到表中。

### 表格提取方法

`pdfplumber.Page`页面对象支持以下方法:

| 方法                                      | 说明                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `.find_tables(table_settings={})`       | 返回表格 `Table` 对象列表. `Table`包含`.cells`, `.rows`,`.bbox` 属性, 以及方法`.extract(x_tolerance=3, y_tolerance=3)` |
| `.extract_tables(table_settings={})`    | 返回从页面上找到的*所有*表中提取的文本，表示为列表列表列表，其结构为“表->行->单元格”。                                                        |
| `.extract_table(table_settings={})`     | 返回从页面上*最大*表中提取的文本，该表表示为列表列表，其结构为“行->单元格”。（如果多个表的大小相同（以单元格数衡量），则此方法将返回最靠近页面顶部的表。）                       |
| `.debug_tablefinder(table_settings={})` | 返回`TableFinder`类的实例，该类可以访问`.edges`(边), `.intersections`(交点), `.cells`(单元格)和`.tables`(表格)属性.            |

举例:

```python
pdf = pdfplumber.open("path/to/my.pdf")
page = pdf.pages[0]
page.extract_table()
```

[查看更多示例](examples/notebooks/extract-table-ca-warn-report.ipynb)

### 表格提取配置

默认情况下， `extract_tables`使用页面的垂直线和水平线（或矩形边）作为单元格分隔符。但该方法可以通过 `table_settings`参数进行高度自定义。以下是设置参数及默认值：

```python
{
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    "snap_tolerance": 3,
    "snap_x_tolerance": 3,
    "snap_y_tolerance": 3,
    "join_tolerance": 3,
    "join_x_tolerance": 3,
    "join_y_tolerance": 3,
    "edge_min_length": 3,
    "min_words_vertical": 3,
    "min_words_horizontal": 1,
    "keep_blank_chars": False,
    "text_tolerance": 3,
    "text_x_tolerance": 3,
    "text_y_tolerance": 3,
    "intersection_tolerance": 3,
    "intersection_x_tolerance": 3,
    "intersection_y_tolerance": 3,
}
```

| 配置项                                                                                    | 说明                                                                                      |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `"vertical_strategy"`                                                                  | 垂直策略,可选值 `"lines"`, `"lines_strict"`, `"text"`, `"explicit"`.见后续说明                      |
| `"horizontal_strategy"`                                                                | 水平策略,可选值 `"lines"`, `"lines_strict"`, `"text"`, `"explicit"`. 见后续说明                     |
| `"explicit_vertical_lines"`                                                            | 明确划分表中单元格的垂直线列表。可与上述任何策略结合使用。列表中的项目应该是数字（表示一条直线的`x`坐标，即页面的全高）或 `line`/`rect`/`curve`对象。 |
| `"explicit_horizontal_lines"`                                                          | 明确划分表中单元格的水平线列表。可与上述任何策略结合使用。列表中的项目应该是数字（表示一条直线的`y`坐标即页面的全高）或 `line`/`rect`/`curve`对象。  |
| `"snap_tolerance"`, `"snap_x_tolerance"`, `"snap_y_tolerance"`                         | `snap_tolerance`像素内的平行线将“捕捉”到相同的水平或垂直位置。                                                |
| `"join_tolerance"`, `"join_x_tolerance"`, `"join_y_tolerance"`                         | 同一条无限线上的线段，其端点在彼此的`join_tolerance`范围内，将“连接”为一条线段                                        |
| `"edge_min_length"`                                                                    | 在尝试重建表之前，将丢弃小于`edge_min_length`的边                                                       |
| `"min_words_vertical"`                                                                 | 使用 `"horizontal_strategy": "text"`时，至少 `min_words_horizontal`单词必须共享相同的对齐方式。             |
| `"min_words_horizontal"`                                                               | 使用 `"horizontal_strategy": "text"`时,至少`min_words_horizontal`单词必须共享相同的对齐方式。              |
| `"keep_blank_chars"`                                                                   | 使用 `text` 策略时, 空格符`" "`将视为单词的一部分而不是单词分隔符                                                |
| `"text_tolerance"`, `"text_x_tolerance"`, `"text_y_tolerance"`                         | 当 `text` 策略搜索单词时，期望每个单词中的单个字母之间的距离不超过`text_tolerance`像素。                                |
| `"intersection_tolerance"`, `"intersection_x_tolerance"`, `"intersection_y_tolerance"` | 将边组合到单元格中时，正交边必须在`intersection_tolerance` 像素范围内才能视为相交。                                  |

### 表格提取策略

`vertical_strategy`(垂直策略) 及 `horizontal_strategy`(水平策略)均包含以下选项:

| 策略               | 说明                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| `"lines"`        | 使用页面的图形线（包括矩形对象的边）作为潜在表格单元格的边框。                                                                              |
| `"lines_strict"` | 使用页面的图形线（而不是矩形对象的边）作为潜在表格单元格的边框。                                                                             |
| `"text"`         | 对于`vertical_strategy`（垂直策略）：推导连接页面上单词的左、右或中心的（假想的）行，并将这些行用作潜在表格单元格的边框。对于`horizontal_strategy`，相同操作，但使用单词的顶部。 |
| `"explicit"`     | 仅使用`explicit_vertical_lines` / `explicit_horizontal_lines`中明确定义的线。                                           |

### 备注

*   在尝试提取表之前裁剪页面通常很有帮助 — `Page.crop(bounding_box)`

*   `v0.5.0`版本的`pdfplumber`针对表格提取功能进行了彻底的重新设计，并引入了突破性的更改。

## 提取表单值

有时PDF文件可以包含表单，包含了人们可以填写和保存的输入。虽然表单字段中的值与PDF文件中的其他文本类似，但表单数据的处理方式不同。如果您想彻底了解详细信息，请参阅本手册第671页 [specification](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdf_reference_archive/pdf_reference_1-7.pdf).

`pdfplumber`没有用于处理表单数据的接口，但您可以使用`pdfplumber`对`pdfminer`的封装组件来访问。

例如，此代码段将检索表单字段名和值，并将它们存储在字典中。您可能需要修改此脚本以处理嵌套字段之类的情况（请参见规范第676页）。

```python
pdf = pdfplumber.open("document_with_form.pdf")

fields = pdf.doc.catalog["AcroForm"].resolve()["Fields"]

form_data = {}

for field in fields:
    field_name = field.resolve()["T"]
    field_value = field.resolve()["V"]
    form_data[field_name] = field_value
```

## 用例演示

*   [提取加利福尼亚工人调整和再培训通知（WARN）报告中的表格](examples/notebooks/extract-table-ca-warn-report.ipynb). 演示基本的可视化调试和表提取。

*   [提取FBI的国家即时刑事背景调查系统PDF文件中的表格](examples/notebooks/extract-table-nics.ipynb). 演示如何使用可视化调试查找最佳的表提取设置。还演示了 `Page.crop(...)`(页面裁剪) 及 `Page.extract_text(...).`(文本导出)

*   [检查和可视化“curve”曲线对象](examples/notebooks/ag-energy-roundup-curves.ipynb).

*   [从圣何塞警察局枪支搜索报告中提取等宽数据](examples/notebooks/san-jose-pd-firearm-report.ipynb), `Page.extract_text(...)`示例.

## 与其他库的比较

其他几个Python库帮助用户从PDF中提取信息。综上所述，`pdfplumber`通过结合以下功能而区别于其他PDF处理库：

*   可以轻松访问每个PDF对象的详细信息

*   拥有用于提取文本和表格的更高级、可自定义的方法

*   集成了可视化调试

*   其他有用的实用功能，例如通过裁剪框过滤对象

了解`pdfplumber`无法提供的功能也很有帮助：

*   创建PDF

*   修改PDF

*   文字识别(OCR)

*   完全支持从OCR识别过的PDF提取表格

### 特性比较

*   [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six) `pdfplumber`是基于该库实现的。它主要关注解析PDF、分析PDF布局和对象定位，以及提取文本。但它不提供用于表提取或可视化调试的工具。

*   [`PyPDF2`](https://github.com/mstamy2/PyPDF2) 是一个纯Python库，“能够拆分、合并、裁剪和转换PDF文件的页面。它还可以向PDF文件添加自定义数据、查看选项和密码。”它可以提取页面文本，但无法轻松访问形状对象（矩形、线条等）、表提取或可视化调试工具。

*   [`pymupdf`](https://pymupdf.readthedocs.io/) 运行速度比`pdfminer`快。可以生成和修改PDF，但该库需要安装非Python软件（MuPDF）。它无法轻松访问形状对象（矩形、直线等），并且不提供表提取或可视化调试工具。

*   [`camelot`](https://github.com/camelot-dev/camelot), [`tabula-py`](https://github.com/chezou/tabula-py), and [`pdftables`](https://github.com/drj11/pdftables) 这些库主要关注表格提取。在某些情况下，它们可能更适合提取特定的表格。


## 认可 / 贡献

非常感谢以下提供了想法、功能和修复的用户：

*   [Jacob Fenton](https://github.com/jsfenfen)

*   [Dan Nguyen](https://github.com/dannguyen)

*   [Jeff Barrera](https://github.com/jeffbarrera)

*   [Bob Lannon](https://github.com/boblannon)

*   [Dustin Tindall](https://github.com/dustindall)

*   [@yevgnen](https://github.com/Yevgnen)

*   [@meldonization](https://github.com/meldonization)

*   [Oisín Moran](https://github.com/OisinMoran)

*   [Samkit Jain](https://github.com/samkit-jain)

*   [Francisco Aranda](https://github.com/frascuchon)

*   [Kwok-kuen Cheung](https://github.com/cheungpat)

*   [Marco](https://github.com/ubmarco)

*   [Idan David](https://github.com/idan-david)

*   [@xv44586](https://github.com/xv44586)

*   [Alexander Regueiro](https://github.com/alexreg)

*   [Daniel Peña](https://github.com/trifling)

*   [@bobluda](https://github.com/bobluda)

*   [@ramcdona](https://github.com/ramcdona)

*   [@johnhuge](https://github.com/johnhuge)

*   [Jhonatan Lopes](https://github.com/jhonatan-lopes)

*   [Ethan Corey](https://github.com/ethanscorey)

*   [Shannon Shen](https://github.com/lolipopshock)

## 贡献者

欢迎贡献代码，由于该库正在积极维护, 请先提交提案

主要维护者:

*   [Jeremy Singer-Vine](https://github.com/jsvine)

*   [Samkit Jain](https://github.com/samkit-jain)
