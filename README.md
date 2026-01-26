<div align="center">

[![License](https://img.shields.io/github/license/Avielzi/whatsapp-api-guide?style=for-the-badge&logo=github&color=dfb317&labelColor=262626)](https://github.com/Avielzi/whatsapp-api-guide/blob/master/LICENSE)

[**עברית**](#-עברית-hebrew) | [**English**](#english)

</div>

---

# 🇮🇱 עברית (Hebrew)

# מדריך מקיף לשימוש ב-WhatsApp Business API: איך להימנע מחסימת חשבון

## מבוא

מדריך זה נועד לספק למפתחים, בעלי עסקים ומשתמשים פרטיים את הידע והכלים הנדרשים לחיבור בטוח ויעיל ל-WhatsApp Business API. המטרה המרכזית היא לאפשר שליחת הודעות, בין אם למטרות שיווק, שירות או תקשורת אישית, תוך מזעור הסיכון לחסימת החשבון. שימוש לא נכון בפלטפורמה עלול להוביל להגבלות חמורות, ובמקרים קיצוניים אף לחסימה לצמיתות, מה שעלול לפגוע קשות בפעילות העסקית או האישית [1].

המדריך יסקור את הסיכונים המרכזיים, יציג את ההבדלים בין שימוש ישיר ב-API של מטא (פייסבוק) לבין עבודה עם ספקי פתרונות עסקיים (BSPs), יפרט תהליך "חימום" חשבון חדש, ויספק הנחיות ושיטות עבודה מומלצות לשמירה על תקינות החשבון לאורך זמן.

## סיכונים מרכזיים: למה חשבונות נחסמים?

פלטפורמת WhatsApp Business מנוהלת בקפידה על ידי מטא כדי להבטיח חווית משתמש גבוהה ולהילחם בספאם. המערכת האוטומטית של וואטסאפ מנטרת באופן קבוע את פעילות החשבונות, ומסמנת חשבונות המפרים את מדיניות השימוש. הבנת הסיבות הנפוצות לחסימה היא הצעד הראשון במניעתה.

### הפרות מדיניות נפוצות

על פי התיעוד הרשמי של מטא, אלו הן חלק מההפרות הנפוצות ביותר שמובילות להגבלות על חשבונות [1]:

*   **שליחת ספאם:** שליחת הודעות לא רצויות או הודעות בתדירות גבוהה מדי.
*   **סיווג שגוי של תבניות הודעה (Templates):** שימוש בתבנית שיווקית למטרת שירות לקוחות, או להיפך.
*   **תוכן אסור:** קידום או מכירה של מוצרים ושירותים מקטגוריות מסוכנות כמו תוכן למבוגרים, אלכוהול וטבק, סמים, הימולים ותוספי תזונה לא בטוחים.
*   **משוב שלילי ממשתמשים:** אם משתמשים רבים חוסמים את המספר שלכם או מדווחים עליו כספאם, הדבר יפגע קשות ב"דירוג האיכות" של החשבון.

### ענישה הדרגתית

מערכת האכיפה של וואטסאפ פועלת באופן הדרגתי. בדרך כלל, חשבון לא ייחסם לצמיתות באופן מיידי (אלא אם מדובר בהפרות חמורות במיוחד). התהליך כולל מספר שלבים:

| שלב הענישה | משך ההגבלה | מהות ההגבלה |
| :--- | :--- | :--- |
| **אזהרה** | - | קבלת התראה על הפרת מדיניות ספציפית. |
| **הגבלה ראשונית** | 1-3 ימים | חסימת היכולת לשלוח הודעות תבנית (שיווק, שירות, אימות). |
| **הגבלה שנייה** | 5-7 ימים | חסימת היכולת לשלוח *כל* סוג של הודעה. |
| **נעילת חשבון** | לא מוגבל בזמן | חסימה מלאה של שליחת הודעות, ניתנת להסרה רק באמצעות ערעור מוצלח. |
| **השבתה לצמיתות** | קבוע | החשבון מוסר לצמיתות מהפלטפורמה. |

---

# 🇺🇸 English

# Comprehensive Guide to Using WhatsApp Business API: How to Avoid Account Bans

## Introduction

This guide is designed to provide developers, business owners, and private users with the knowledge and tools required for a safe and efficient connection to the WhatsApp Business API. The central goal is to enable message sending, whether for marketing, service, or personal communication purposes, while minimizing the risk of account blocking. Improper use of the platform can lead to severe restrictions, and in extreme cases, even permanent blocking, which can seriously harm business or personal activities [1].

The guide will cover key risks, present the differences between direct use of Meta's (Facebook) API versus working with Business Solution Providers (BSPs), detail a new account "warm-up" process, and provide guidelines and best practices for maintaining account health over time.

## Key Risks: Why Do Accounts Get Blocked?

The WhatsApp Business platform is carefully managed by Meta to ensure a high user experience and fight spam. WhatsApp's automated system regularly monitors account activity and flags accounts that violate usage policies. Understanding the common reasons for blocking is the first step in preventing it.

### Common Policy Violations

According to Meta's official documentation, these are some of the most common violations that lead to account restrictions [1]:

*   **Sending Spam:** Sending unwanted messages or messages too frequently.
*   **Incorrect Classification of Message Templates:** Using a marketing template for customer service purposes, or vice versa.
*   **Prohibited Content:** Promoting or selling products and services from restricted categories such as adult content, alcohol and tobacco, drugs, gambling, and unsafe supplements.
*   **Negative User Feedback:** If many users block your number or report it as spam, this will severely damage the account's "Quality Rating."

### Gradual Enforcement

WhatsApp's enforcement system operates gradually. Usually, an account will not be permanently blocked immediately (unless it's a particularly serious violation). The process includes several stages:

| Enforcement Stage | Restriction Duration | Nature of Restriction |
| :--- | :--- | :--- |
| **Warning** | - | Receiving a notification about a specific policy violation. |
| **Initial Restriction** | 1-3 days | Blocking the ability to send template messages (marketing, service, authentication). |
| **Second Restriction** | 5-7 days | Blocking the ability to send *any* type of message. |
| **Account Lock** | Indefinite | Full blocking of message sending, can only be removed through a successful appeal. |
| **Permanent Disabling** | Permanent | The account is permanently removed from the platform. |

---

## 🌍 Languages & Localization

This guide is available in multiple languages:

- **עברית (Hebrew)** - Full guide in Hebrew with full RTL support.
- **English** - Complete guide in English with full LTR support.

---

## 📋 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Developed by **Aviel.AI** - All Rights Reserved © 2026
