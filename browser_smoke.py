from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
html=(p/'index.html').read_text(encoding='utf8').replace('<link rel="stylesheet" href="./styles.css">','<style>'+(p/'styles.css').read_text(encoding='utf8')+'</style>').replace('<script defer src="./game.js"></script>','').replace('</body>','<script>'+(p/'game.js').read_text(encoding='utf8')+'</script></body>')
with sync_playwright() as b:
 browser=b.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for size in [(1300,900),(390,844)]:
  page=browser.new_page(viewport={'width':size[0],'height':size[1]})
  errors=[];page.on('pageerror', lambda e:errors.append(str(e)))
  page.set_content(html,wait_until='domcontentloaded')
  assert page.get_by_role('button',name='Begin het avontuur').count()==1
  page.get_by_role('button',name='Begin het avontuur').click()
  assert page.locator('.age-card').count()==3
  page.locator('[data-age="6"]').click()
  assert page.locator('.world-card').count()==8
  page.screenshot(path=str(p/('map-mobile.png' if size[0]<500 else 'map.png')),full_page=True)
  page.locator('[data-world="letters1"]').click()
  assert page.locator('.level-tile').count()==7
  page.locator('[data-level="0"]').click()
  assert page.locator('.letter-stage').count()==1
  page.locator('[data-action="start-quiz"]').click()
  for _ in range(12):
   if page.locator('.reward').count():break
   if page.locator('#trace').count():
    box=page.locator('#trace').bounding_box()
    page.mouse.move(box['x']+15,box['y']+15)
    page.mouse.down();page.mouse.move(box['x']+40,box['y']+65);page.mouse.up()
    page.locator('[data-action="trace-done"]').click()
   else:
    page.evaluate('''() => {const q=questions[qi];const index=q.options.findIndex(o=>o.value===q.correct);document.querySelectorAll('[data-action="answer"]')[index].click()}''')
    page.locator('[data-action="next-question"]').click()
  assert page.locator('.reward').count()==1, 'reward missing'
  assert page.locator('.reward-stars').inner_text()=='★★★',page.locator('.reward-stars').inner_text()
  assert len(errors)==0,errors
  page.screenshot(path=str(p/('reward-mobile.png' if size[0]<500 else 'reward.png')),full_page=True)
  print('PASS browser UI',size,'star-count',page.locator('.stars-counter').inner_text())
  page.close()
 browser.close()