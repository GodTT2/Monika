import discord
from discord.ext import commands
import io
import textwrap
import traceback
from contextlib import redirect_stdout

class Developer:

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')

    @commands.command(name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates code."""
        try:
            r = eval(cleanup_code(body))
        except Exception as e:
            await ctx.send(f'```py\n{type(e).__name__}: {e}\n```')
        else:
            await ctx.send(f'```py\n{e}\n```')

def setup(bot):
    bot.add_cog(Developer(bot))