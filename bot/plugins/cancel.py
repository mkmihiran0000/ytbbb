from pyrogram import filters as Filters

from ..utubebot import UtubeBot


@UtubeBot.on_callback_query(Filters.create(lambda _, __, query: query.data.startswith('cncl+')))
async def cncl(c, q):
    _, pid = q.data.split('+')
    if not c.download_controller.get(pid, False):
        await q.answer("🤖Your process is not currently active👀", show_alert=True)
        return
    c.download_controller[pid] = False
    await q.answer("🔴Your process will be cancelled soon🔴", show_alert=True)
