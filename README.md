# rise-python-nostr
Learning how to build a distributed system via nostr protocol in RISE program

# Command
    source nostr/bin/activate
    python client-sender.py --host relay.nekolicio.us --message "HelloWorld"


# Phase 1 Q&A
> What are some of the challenges you faced while working on Phase 1?
- Understanding the basic nostr protocol
- Installing the virtual environment in Mac OS for package installment
- Understanding how to connecting to the provided server
> What kind of failures do you expect to a project such as DISTRISE to encounter?
- When we use event aggregator to deal with multiple relay requests in the same time, it may cause latency and consistency issue in the progress

# Phase 2 Q&A
> Why did you choose this database?
- 
> If the number of events to be stored will be huge, what would you do to scale the database?
- 
# Material Ref
- [Project Introduction](https://achq.notion.site/Distributed-Systems-Project-Briefing-00eaa7a219954bb1a346d73bf09164f2)
- [NIP-protocol](https://github.com/nostr-protocol/nips/blob/master/01.md)
- [Github:python-nostr](https://github.com/jeffthibault/python-nostr)
- [Github:postr](https://github.com/Happyzippy/postr)
- [Github:nostr_relay](https://github.com/davestgermain/nostr_relay)