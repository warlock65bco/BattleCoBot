    @commands.command(help="Use this command to clear the WS Queue, to start the WS")
    async def start(self, ctx, message, confirm=None):
        msg = []
        if (message == '1') or (message == '2'):
            db = sqlite3.connect('roster.sqlite')
            cursor = db.cursor()
            sql = "SELECT roster FROM main WHERE roster=?"
            cursor.execute(sql, message)
            results = cursor.fetchall()
            print(results)
            if (len(results) != 0):
                if(len(results) % 5 == 0) and (len(results) < 16):
                    sql = "DELETE FROM main WHERE roster=?"
                    cursor.execute(sql, message)
                    db.commit()
                    cursor.close()
                    db.close()
                    msg.append(await ctx.send(f"The WS roster #{message} has been cleared, best of luck!"))
                elif(confirm == 'clear'):
                    sql = "DELETE FROM main WHERE roster=?"
                    cursor.execute(sql, message)
                    db.commit()
                    cursor.close()
                    db.close()
                    msg.append(await ctx.send(f"The WS roster #{message} has been cleared, best of luck!"))
                else:
                    msg.append(await ctx.send(f"The WS Roster #{message} doesn't have 5, 10, or 15, people. However, you can override this by adding clear to this command"))
            else:
                msg.append(await ctx.send(f"There is nobody in WS Roster #{message}"))
        else:
            msg.append(await ctx.send("There are only two rosters, so use !start 1 or !start 2"))
        await asyncio.sleep(20)
        await ctx.message.delete()
        for ms in msg:
            await ms.delete()
            
            
            
            
            
            role = get(member.guild.roles, name="WS_Squad_"+message)
            db = sqlite3.connect('roster.sqlite')
            cursor = db.cursor()
            sql = "SELECT nickname FROM main WHERE roster=?"
            cursor.execute(sql, roster)
            result = cursor.fetchall()
            if len(results) != 0:
                people = []
                    for result in results:
                        result = str(result)
                        result = result[2:]
                        result = result[:len(result)-3]
                        people.append(result)
                    roster_embed = discord.Embed(
                        description = (f'The current roster for WS Roster #{message}'),
                        colour = discord.Colour.teal()
                    )
                    roster_embed.set_footer(text='Best of luck on this WS!')
                    number = 1
                    for person in people:
                        roster_embed.add_field(name=f'Player #{number}', value=f'{person}', inline=False)
                        number += 1
                    embed_msg = await ctx.send(embed=roster_embed)
                    msg = await ctx.send(f"You have been added to WS Roster #{message}")
                #for member in ctx.guild.members:
                    #if member.nick == user_nickname:
                        user = member
                        await user.add_roles(role)
                        #print(user)
                #member = user_nickname
                
                
