from PIL import Image
import json

def Picture_Synthesis(mother_img,
                      son_img,
                      save_img,
                      coordinate=None):
    """
    :param mother_img: 母图
    :param son_img: 子图
    :param save_img: 保存图片名
    :param coordinate: 子图在母图的坐标
    :return:
    """
    #将图片赋值,方便后面的代码调用
    M_Img = Image.open(mother_img)
    S_Img = Image.open(son_img)

    #给图片指定色彩显示格式
    M_Img = M_Img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）

    # 获取图片的尺寸
    M_Img_w, M_Img_h = M_Img.size  # 获取被放图片的大小（母图）
    print("母图尺寸：",M_Img.size)
    S_Img_w, S_Img_h = S_Img.size  # 获取小图的大小（子图）
    print("子图尺寸：",S_Img.size)

    expect_w = coordinate[2]-coordinate[0]

    expect_h = coordinate[3]-coordinate[1]

    if M_Img_w < coordinate[2] or M_Img_h < coordinate[3]:
        print('坐标错误')

    if S_Img_w > expect_w or S_Img_h > expect_h:


        icon = S_Img.resize((expect_w, expect_h), Image.ANTIALIAS)




    M_Img.paste(icon, coordinate, mask=None)

    # 保存图片
    M_Img.save(save_img)


with open('/Users/lzy/PycharmProjects/company_interview/boxes.json','r',encoding='utf8') as f:
    json_data = json.load(f)
    dic = json_data
    boxes = dic['boxes']
    for box in boxes:
        if box['name'] == 'box_b':
            left_top = box['rectangle']['left_top']
            right_bottom = box['rectangle']['right_bottom']
            break
        else:
            continue

coordinate = tuple(left_top) + tuple(right_bottom)
print(coordinate)

Picture_Synthesis(mother_img='/Users/lzy/Desktop/kobe1.png',
                  son_img="/Users/lzy/Desktop/kobe2.png",
                  save_img="/Users/lzy/Desktop/kobe4.png",
                  coordinate=coordinate
                 )
