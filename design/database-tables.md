# Database Tables

        database:   sqlite3
        dialect:    sql
        charset:    utf8

---

> **NOTE** : all tables have `id`,`created_at`,`updated_at` fields which will not be shown below.

## Users

    - avatar    <string>,   # location of file to be kept
    - fname     <string>,
    - lname     <string>,
    - email     <string>(unique),
    - website   <string>
    - password  <string>,
    - type      <string>    [ admin, employer, employee ],
    - city      <string>    # these 3 make up the address for simplicity {city, county, street}
    - country   <string>
    - street    <string>
    - status    <string> [active, banned]

## Qualifications

    - userId,   <string>(unique)
    - details,  <string>
    - website   <string>

## Companies

    - avatar,   <string>    # location metadata of file to be kept
    - name,     <string>
    - website,  <string>
    - city      <string>
    - country   <string>
    - street    <string>
    - bio,      <string>
    - email,    <string>
    - password, <string>
    - industry, <string> [list from 19 items, in file: `text-content.md` heading:INDUSTRIES]
    - sector,   <string>    
    - status    <string>     [active, banned]
    - 

## Jobs

    - name,         <string>
    - email,        <string>
    - salary,       <string>  [used string to cater for ranges and other specifics]
    - offsite_link,     <string>
    - published_on      <date>
    - expires,      <date>
    - duration,     <string>
    - position      <string>   
    - type          <string[]> [remote, office, hybrid]
    - documents         <string[]> [cv, resume, application-letter, motivation-letter]
    - status        <string>   [standby, waiting, draft, published, approved, denied]

## Messages

    - ownerId,      <number>
    - recipientId,  <number>
    - content,      <string>
    - created,      <date>
    - updated       <date>

## applications

    - user_id,    <number>
    - company_id, <number>
    - favorite,  <bool>
    - applied_on, <date>
    - status     <string>   [waiting, hold, approved, denied,cancelled]
    - type       <string>   [office, remote, hybrid]

## files

    - tag               <string> [avatar, resume, cv, ...]
    - metadata          <string>
    - extension         <string> [jpeg, png, pdf, doc, ...]
    - owner_id          <number>
    - application_id    <string>
    - location          <string>

## reports

    - reporter_id    <number>
    - content_id        <number>
    - type          <string> [job_post, job_application]
    - details       <string>
    - created       <date>
    - updated       <date>

## notifications

    - ownerId,      <number>
    - recipientId,  <number>
    - content,      <string>
    - created,      <date>
    - updated       <date>
    - status        <string> [opened,new,marked]