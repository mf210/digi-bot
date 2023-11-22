import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class InsBot:
    def __init__(self) -> None:
        options = Options()
        # options.add_argument("--remote-debugging-port=9222")
        options.add_argument('--profile-directory=Profile 1')
        options.add_argument("user-data-dir=C:\\Users\\matt\\AppData\\Local\\Google\\Chrome\\User Data\\") #Path to your chrome profile
        self.driver = webdriver.Chrome(options=options)
        # self.driver.get("https://www.digikala.com/search/category-headphone/?has_selling_stock=1&page=1&sort=7")
        self.driver.get("https://www.digikala.com/product/dkp-2891227/%D9%87%D8%AF%D9%81%D9%88%D9%86-%DA%A9%DB%8C%D9%88-%DA%A9%DB%8C-%D8%B2%D8%AF-%D9%85%D8%AF%D9%84-ak6/#gallery")

        sleep(3)
    
    def get_product_links(self):
        product_links = self.driver.find_elements(By.CSS_SELECTOR, 'a.block.cursor-pointer.relative.bg-neutral-000.overflow-hidden.grow.py-3.px-4.lg\\:px-2.h-full.styles_VerticalProductCard--hover__ud7aD')
        for link in product_links:
            product_url = link.get_attribute('href')
            print(product_url)
        
    
    def get_product_image_links(self):

        parent_div = self.driver.find_element(By.CSS_SELECTOR, 'div.flex.flex-wrap')

        # Find all img tags within the parent div
        image_tags = parent_div.find_elements(By.CSS_SELECTOR, 'img')

        # Extract and print the image URLs from each img tag
        for img_tag in image_tags:
            image_url = img_tag.get_attribute('src')
            print(image_url)



        # image_divs = self.driver.find_elements(By.CSS_SELECTOR, 'div.overflow-hidden.overflow-hidden.rounded.cursor-pointer.bg-neutral-000.ml-2.lg\:mb-3.flex.items-center.styles_ProductImagesModal__productImage__fzbFF.styles_ProductImagesModal__productImage--selected__Of_7l')

        # # Extract and print the image URLs from each div tag
        # for div in image_divs:
        #     # Find the img tag within the div
        #     img_tag = div.find_element(By.CSS_SELECTOR,'img')

        #     # Extract the src attribute (image URL)
        #     image_url = img_tag.get_attribute('src')
        #     print(image_url)


    # def like_homepage_posts(self):
    #     self.driver.implicitly_wait(10)
    #     posts = self.driver.find_elements(By.XPATH, "//article[contains(@class, '_ab6k')]")
    #     print(f'############ posts:{len(posts)} ############')
    #     for post in posts[:5]:  # Loop through the first five posts
    #         # print('post', post)
    #         like_button = post.find_element(By.CLASS_NAME, '_aamw')  # Replace 'like-button' with the class name of the like button
    #         ActionChains(self.driver).move_to_element(like_button).click().perform()
    #         sleep(2)  # Add a delay between each like

    #     sleep(10)




my_bot = InsBot()
# my_bot.get_product_link()
my_bot.get_product_image_links()

# #gallery
# <div class="product-list_ProductList__item__LiiNI" data-product-index="2"><a class="block cursor-pointer relative bg-neutral-000 overflow-hidden grow py-3 px-4 lg:px-2 h-full styles_VerticalProductCard--hover__ud7aD" target="_blank" href="/product/dkp-5013379/%D9%87%D8%AF%D9%81%D9%88%D9%86-%D8%A8%D9%84%D9%88%D8%AA%D9%88%D8%AB%DB%8C-%D9%85%D8%AF%D9%84-k55/"><div data-testid="product-card" class="h-full"><article class="overflow-hidden flex flex-col items-stretch justify-start h-full"><div class="flex items-center justify-start mb-1"><div class="text-body2-extra grow"><br></div></div><div class="flex grow relative flex-col"><div class=""><div class="flex items-stretch flex-col relative mb-1"><div class="flex items-start mx-auto"><div><div style="width: 240px; height: 240px; line-height: 0;"><picture><source type="image/webp" srcset="https://dkstatics-public.digikala.com/digikala-products/0ebd9704b803f36a9738fd0cb9ace5adf85c1beb_1678780833.jpg?x-oss-process=image/resize,m_lfit,h_300,w_300/format,webp/quality,q_80"><source type="image/jpeg" srcset="https://dkstatics-public.digikala.com/digikala-products/0ebd9704b803f36a9738fd0cb9ace5adf85c1beb_1678780833.jpg?x-oss-process=image/resize,m_lfit,h_300,w_300/quality,q_80"><img class="w-full rounded-medium inline-block" src="https://dkstatics-public.digikala.com/digikala-products/0ebd9704b803f36a9738fd0cb9ace5adf85c1beb_1678780833.jpg?x-oss-process=image/resize,m_lfit,h_300,w_300/quality,q_80" width="240" height="240" alt="هدفون بلوتوثی مدل K55" title="" style="object-fit: contain;"></picture></div></div><div class="flex items-center justify-center gap-2 absolute top-0 left-0 flex-col p-1 bg-neutral-000 style_ProductImage__colors--topLeft__iHRie"><span class="rounded-circle inline-block color_Color__l0PYL" style="background-color: rgb(33, 33, 33); width: 8px; height: 8px;"></span></div></div></div></div><div class="grow flex flex-col items-stretch justify-start"><div class="flex items-center justify-start gap-1 flex-wrap mb-1"><br><br></div><div><h3 class="ellipsis-2 text-body2-strong text-neutral-700 styles_VerticalProductCard__productTitle__6zjjN">هدفون بلوتوثی مدل K55</h3></div><div class="mb-1 flex items-center justify-between"><div class="flex items-center" data-ab-id=""><div class="flex shrink-0 ml-1"><svg style="width: 18px; height: 18px; fill: var(--color-delivery-jet-expansion);"><use xlink:href="#deliveryToday"></use></svg></div><p class="text-caption text-neutral-600">ارسال امروز</p><br></div><div class="flex items-center"><p class="text-body2-strong text-neutral-700">۴.۳</p><div class="flex mr-2 shrink-0"><svg style="width: 16px; height: 16px; fill: var(--color-icon-rating-0-2);"><use xlink:href="#starFill"></use></svg></div></div></div><div class="pt-1 flex flex-col items-stretch justify-between"><div class="flex items-center justify-between"><div class="flex items-center justify-end gap-1 text-neutral-700 text-neutral-400 text-h5 grow"><span data-testid="price-final">۴۶۵,۰۰۰</span><div class="flex"><svg style="width: 16px; height: 16px; fill: var(--color-icon-high-emphasis);"><use xlink:href="#toman"></use></svg></div></div></div><div class="flex items-center justify-between pl-5"></div></div></div></div></article></div></a></div>