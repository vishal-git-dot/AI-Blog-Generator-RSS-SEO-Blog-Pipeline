---
title: "Learnt Git Rebasing the hard way"
slug: "learnt-git-rebasing-the-hard-way"
author: "Satwik Sai Prakash Sahoo"
source: "devto_ai"
published: "Wed, 19 Aug 2026 12:49:35 +0000"
description: "Hello again! Weeks 9 and 10 covered the fourth estimator family, the first release that carries my work, and a git mess that taught me more than the code did..."
keywords: "you, builder, one, git, base, which, branch, than"
generated: "2026-08-19T12:56:23.251082"
---

# Learnt Git Rebasing the hard way

## Overview

Hello again! Weeks 9 and 10 covered the fourth estimator family, the first release that carries my work, and a git mess that taught me more than the code did. PR #1920 merged, and sbi 0.27 shipped First, the ratio estimator builder from my last post made it in, together with the whole base class hardening bundle. Right after that, sbi 0.27 was released and PRs 1 to 5 were ported over to main . So the typed builder API is now actually in a release, for NPE, NLE, MNPE, MNLE and all four NRE variants. That also means the free rename window is closed. The z_score_input and z_score_condition names we picked in week 7 are now the shipped names, which is exactly why we did that rename when we did. Writing the design before the code Under the new workflow I described last time, the vector field work started with a markdown file instead of a Python file. The vector field family is genuinely harder than the others. build_vector_field_estimator picks along what looks like three axes at the same time: whether you want flow matching or score matching, which SDE type you want if it is score matching, and which network architecture sits inside. And unlike every other family, there are no per-model build functions to hang a config class on. I wrote up the options with some open questions then my mentor, Jan reviewed it and we settled on one builder with a base class abstraction to cut the redundancy across builders. Doing this on paper first was clearly the right call. Some of the things I had assumed while writing the proposal turned out to be wrong, and finding that out in a review comment on a markdown file was a lot cheaper than finding it out in a review comment on 800 lines of code. PR #1921 : VectorFieldEstimatorBuilder With the design agreed, the implementation covers FMPE and NPSE. The builder takes the architecture as model , one of mlp , ada_mlp , transformer or transformer_cross_attn , plus estimator_type for flow versus score and sde_type for the noise schedule. One detail I liked: this family has fields that only make sense for one side. sigma_min , sigma_max and the schedule settings belong to score estimators, and gaussian_baseline belongs to flow matching. So the builder raises if you set a score field with estimator_type="flow" , and the other way round. Interestingly the raw build_vector_field_estimator function does not do that. It silently ignores sde_type if you asked for flow matching. So the builder is stricter than the function it wraps, which is the whole point of this project in one sentence. I also kept the applicability lists deliberately small and added tests that check them against the existing config classes, so the two cannot drift apart without CI noticing. The rebasing lesson Now for the part that actually cost me time. PR #1921 was branched off PR #1920 , which was branched off earlier work. As PR #1920 changed during review, I kept merging main back into my branch to stay current. What I ended up with was a branch history full of merge commits and small repair commits, and when it came time to present a clean PR, replaying that history with git rebase was painful. Every conflict I had already resolved once came back to be resolved again. The thing that finally worked, and what Jan uses too, is to stop trying to replay history at all: git reset --soft <clean base> git commit --soft keeps your working tree exactly as it is and just moves the branch pointer, so you get the final state of your code sitting on a clean base, and then you commit it in whatever shape makes sense for a reviewer. All the intermediate mess disappears because you never replay it. The other half of the lesson is that sbi squash merges its PRs. I had assumed that once PR #1920 merged, its commits would stop showing up in PR #1921 's diff on their own. They do not. Squash merging creates a brand new commit on main , so my branch's merge base never moves and those commits keep appearing until I explicitly rebase onto the new main : git rebase --onto upstream/main <old base> <my branch> I now understand a lot better why maintainers care so much about branch hygiene. A reviewer opening a PR with 40 commits, half of which belong to a different PR, is going to have a bad time no matter how good the actual code is. Also decided Two smaller things from the week 9 sync. Keyword harmonization is moving to the documentation PR rather than the vector field PR, so the VF PR stays focused and we do not break tutorials in the same change. And the work order for the rest of the project is now: vector field PR, then test refactoring, then documentation. What's Next? PR #1921 is in review. After that comes the marginal estimator builder, and then the documentation PR. There is also a growing pile of test files, one per PR at this point, that we plan to consolidate once everything has merged. Thanks for following along, and see you in the next one!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/satwiksps/learnt-git-rebassing-the-hard-way-2dmd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
