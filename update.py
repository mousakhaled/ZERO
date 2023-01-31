# This file didn't used in the userbot because it has error
import threading
import contextlib
import os
from asyncio import CancelledError
import heroku3
from asyncio import CancelledError
from telethon import events
from sqlalchemy.ext.declarative import declarative_base
import logging
from asyncio import CancelledError
from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, PickleType, UnicodeText
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import heroku3
from sqlalchemy.orm import sessionmaker, scoped_session
plugin_category = "tools"
ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger(__name__)
# -- Constants -- #

HEROKU_APP_NAME = "usjsubot"
HEROKU_API_KEY = "93f2cff4-1b3b-401d-9f81-a06092a1ae4d"
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[
    HEROKU_APP_NAME
]
UPSTREAM_REPO_BRANCH = "https://github.com/perdark/per-sed"

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "main"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/main"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
engine = create_engine("sqlite:///xdexer.db", echo=False)


def start() -> scoped_session:
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()


class Cat_GlobalCollection(BASE):
    __tablename__ = "sed_connection"
    keywoard = Column(UnicodeText, primary_key=True)
    contents = Column(PickleType, primary_key=True, nullable=False)

    def __init__(self, keywoard, contents):
        self.keywoard = keywoard
        self.contents = tuple(contents)

    def __repr__(self):
        return "<Cat Global Collection lists '%s' for %s>" % (
            self.contents,
            self.keywoard,
        )

    def __eq__(self, other):
        return (
            isinstance(other, Cat_GlobalCollection)
            and self.keywoard == other.keywoard
            and self.contents == other.contents
        )


BASE.metadata.create_all(engine)

Cat_GlobalCollection.__table__.create(checkfirst=True)

CAT_GLOBALCOLLECTION = threading.RLock()


class COLLECTION_SQL:
    def __init__(self):
        self.CONTENTS_LIST = {}


COLLECTION_SQL_ = COLLECTION_SQL()


def add_to_collectionlist(keywoard, contents):
    with CAT_GLOBALCOLLECTION:
        keyword_items = Cat_GlobalCollection(keywoard, tuple(contents))

        SESSION.merge(keyword_items)
        SESSION.commit()
        COLLECTION_SQL_.CONTENTS_LIST.setdefault(
            keywoard, set()).add(tuple(contents))


def get_collectionlist_items():
    try:
        chats = SESSION.query(Cat_GlobalCollection.keywoard).distinct().all()
        return [i[0] for i in chats]
    finally:
        SESSION.close()


def del_keyword_collectionlist(keywoard):
    with CAT_GLOBALCOLLECTION:
        keyword_items = (
            SESSION.query(Cat_GlobalCollection.keywoard)
            .filter(Cat_GlobalCollection.keywoard == keywoard)
            .delete()
        )
        COLLECTION_SQL_.CONTENTS_LIST.pop(keywoard)
        SESSION.commit()


logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

LOGS = logging.getLogger(__name__)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is None:
        return await event.edit("`Please set up`  **HEROKU_API_KEY**  ` Var...`")
    heroku = heroku3.from_key(HEROKU_API_KEY)
    heroku_applications = heroku.apps()
    if HEROKU_APP_NAME is None:
        await event.edit(
            "`Please set up the` **HEROKU_APP_NAME** `Var`"
            " to be able to deploy your userbot...`"
        )
        repo.__del__()
        return
    heroku_app = next(
        (app for app in heroku_applications if app.name == HEROKU_APP_NAME),
        None,
    )

    if heroku_app is None:
        await event.edit(
            f"{txt}\n" "`Invalid Heroku credentials for deploying userbot dyno.`"
        )
        return repo.__del__()
    sandy = await event.edit(
        "`Userbot dyno build in progress, please wait until the process finishes it usually takes 4 to 5 minutes .`"
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    ups_rem.fetch(ac_br)
    repo.git.reset("--hard", "FETCH_HEAD")
    heroku_git_url = heroku_app.git_url.replace(
        "https://", f"https://api:{HEROKU_API_KEY}@"
    )

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(heroku_git_url)
    else:
        remote = repo.create_remote("heroku", heroku_git_url)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Error log:**\n`{error}`")
        return repo.__del__()
    build_status = heroku_app.builds(order_by="created_at", sort="desc")[0]
    if build_status.status == "failed":
        return await event.edit(
            "`Build failed!\n" "Cancelled or there were some errors...`"
        )
    try:
        remote.push("master:main", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Here is the error log:**\n`{error}`")
        return repo.__del__()
    await event.edit("`Deploy was failed. So restarting to update`")
    with contextlib.suppress(CancelledError):
        await event.client.disconnect()
        if HEROKU_APP is not None:
            HEROKU_APP.restart()


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة السورس"))
async def _(event):
    event = await event.edit("`Pulling the nekopack repo wait a sec ....`")
    off_repo = "https://github.com/TgCatUB/nekopack"
    os.chdir("/app")
    try:
        txt = (
            "`Oops.. Updater cannot continue due to "
            + "some problems occured`\n\n**LOGTRACE:**\n"
        )

        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ac_br = repo.active_branch.name
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    await event.edit("`Deploying userbot, please wait....`")
    await deploy(event, repo, ups_rem, ac_br, txt)