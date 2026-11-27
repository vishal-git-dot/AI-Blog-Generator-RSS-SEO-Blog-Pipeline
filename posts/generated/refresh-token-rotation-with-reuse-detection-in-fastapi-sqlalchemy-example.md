---
title: "Refresh token rotation with reuse detection in FastAPI (SQLAlchemy example)"
slug: "refresh-token-rotation-with-reuse-detection-in-fastapi-sqlalchemy-example"
author: "LaunchPad Kits"
source: "devto_python"
published: "Fri, 27 Nov 2026 20:37:40 +0000"
description: "Long-lived refresh tokens are the weak point of JWT auth: if one leaks, the attacker can mint access tokens until it expires. Rotation plus reuse detection l..."
keywords: "refresh, token, family, true, row, refreshtoken, mapped, none"
generated: "2026-11-27T20:56:45.959653"
---

# Refresh token rotation with reuse detection in FastAPI (SQLAlchemy example)

## Overview

Long-lived refresh tokens are the weak point of JWT auth: if one leaks, the attacker can mint access tokens until it expires. Rotation plus reuse detection limits the damage. Here is a compact implementation with FastAPI and async SQLAlchemy. The idea Every refresh token has a unique id ( jti ) and belongs to a family , which is created at login. Each refresh token is single use . Calling /refresh revokes the old token and issues a new one in the same family. If a token that was already revoked shows up again, someone replayed it (the legitimate client or the thief used it first). Revoke the whole family , which logs out both. The model The server keeps a record of every issued refresh token. Only the id is stored, never the token itself. class RefreshToken ( Base ) : __tablename__ = "refresh_tokens" id : Mapped [ int ] = mapped_column ( primary_key = True ) jti : Mapped [ str ] = mapped_column ( String ( 64 ) , unique = True , index = True ) family : Mapped [ str ] = mapped_column ( String ( 64 ) , index = True ) user_id : Mapped [ int ] = mapped_column ( ForeignKey ( "users.id" , ondelete = "CASCADE" ) , index = True ) expires_at : Mapped [ datetime ] = mapped_column ( DateTime ( timezone = True ) ) revoked_at : Mapped [ datetime | None ] = mapped_column ( DateTime ( timezone = True ) ) The token The JWT carries sub , type , jti and fam . Access tokens use a different type , and decoding checks it, so an access token cannot be used as a refresh token. The endpoint @router . post ( "/refresh" , response_model = TokenPair ) async def refresh ( data : RefreshIn , session = Depends ( get_session ) , settings = Depends ( get_settings_dep ) ) : bad = HTTPException ( 401 , "Invalid refresh token" ) try : payload = decode_token ( settings , data . refresh_token , "refresh" ) except jwt . PyJWTError : raise bad from None row = await session . scalar ( select ( RefreshToken ) . where ( RefreshToken . jti == payload [ "jti" ] ) ) if row is None : raise bad if row . revoked_at is not None : # Reuse detected: assume theft, revoke every token in the family. await session . execute ( update ( RefreshToken ) . where ( RefreshToken . family == row . family , RefreshToken . revoked_at . is_ ( None ) ) . values ( revoked_at = utcnow ( ) ) ) await session . commit ( ) raise bad user = await session . get ( User , row . user_id ) if user is None or not user . is_active : raise bad row . revoked_at = utcnow ( ) return await _issue_pair ( session , settings , user , family = row . family ) Notes: Every failure returns the same 401, so callers learn nothing about why. Commit the family revocation before raising, otherwise the rollback undoes it. Rate-limit the endpoint. On password change or reset, revoke all of the user's refresh tokens. Test it Write the test before trusting it: log in, refresh once (works), refresh again with the first token (401), then check that the second token is also dead. That last assertion is the one people forget. Related checklist The rest of the SaaS plumbing (tenants, API keys, Stripe webhooks, plan limits) is in this checklist: https://extezzu.github.io/webtools/guides/fastapi-saas-backend-checklist/ Disclosure: this code is taken from a commercial FastAPI starter we sell ($29, one-time): https://www.creem.io/product/prod_7LIIfd0Y6cBufZxtRTfNO9 . The snippet above is complete enough to use on its own.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/launchpadkits/refresh-token-rotation-with-reuse-detection-in-fastapi-sqlalchemy-example-15n9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
