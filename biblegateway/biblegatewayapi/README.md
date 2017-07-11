<h1><strong>Unofficial Python API for BibleGateway</strong></h1>

<p><strong>This API implements method for:</strong></p>

<p><strong>get_passage</strong> : search a specific passage (es. John 3:16)</p>

<p>params:</p>

<ul>
	<li>passage: it explain itself</li>
	<li>version: es. ESV numeration: show verse number or not</li>
	<li>title: show passage title or not</li>
</ul>

<p>output:</p>

<ul>
	<li>dictionary(reference,version,text)</li>
</ul>

<p><strong>get_search_results</strong><em> :&nbsp;</em><span style="line-height: 1.6;">search specific words (es. Fruit Spirit) </span></p>

<p><span style="line-height: 1.6;">params: </span></p>

<ul>
	<li><span style="line-height: 1.6;">search: words to search version: es. ESV </span></li>
	<li><span style="line-height: 1.6;">searchype: Possible search type ALL, ANY, PHRASE </span></li>
</ul>

<p><span style="line-height: 1.6;">output: </span></p>

<ul>
	<li><span style="line-height: 1.6;">dictionary(reference,text) </span></li>
</ul>

<p><span style="line-height: 1.6;"><strong>getVOTD</strong> : show verse of the day </span></p>

<p><span style="line-height: 1.6;">params: </span></p>

<ul>
	<li><span style="line-height: 1.6;">version: es. ESV </span></li>
</ul>

<p><span style="line-height: 1.6;">output: </span></p>

<ul>
	<li><span style="line-height: 1.6;">dictionary(reference,version,text) </span></li>
</ul>

<h2><span style="line-height: 1.6;">Execution of Example.py</span></h2>

<pre>
<span style="line-height: 1.6;"><strong>****** Result for passage John 3:1-15 ******** </strong></span>

<span style="line-height: 1.6;">Reference :John 3:1-15</span>

<span style="line-height: 1.6;">Version :ESV </span>

<span style="line-height: 1.6;">You Must Be Born Again </span>

<span style="line-height: 1.6;">3 </span>

<span style="line-height: 1.6;">Now there was a man of the Pharisees named Nicodemus, a ruler of the Jews. &sup2;This man came to Jesus by night and said to him, &ldquo;Rabbi, we know that you are a teacher come from God, for no one can do these signs that you do unless God is with him.&rdquo; &sup3;Jesus answered him, &ldquo;Truly, truly, I say to you, unless one is born again he cannot see the kingdom of God.&rdquo; ⁴Nicodemus said to him, &ldquo;How can a man be born when he is old? Can he enter a second time into his mother&#39;s womb and be born?&rdquo; ⁵Jesus answered, &ldquo;Truly, truly, I say to you, unless one is born of water and the Spirit, he cannot enter the kingdom of God. ⁶That which is born of the flesh is flesh, and that which is born of the Spirit is spirit. ⁷Do not marvel that I said to you, &lsquo;You must be born again.&rsquo; ⁸The wind blows where it wishes, and you hear its sound, but you do not know where it comes from or where it goes. So it is with everyone who is born of the Spirit.&rdquo;⁹Nicodemus said to him, &ldquo;How can these things be?&rdquo; &sup1;⁰Jesus answered him, &ldquo;Are you the teacher of Israel and yet you do not understand these things? &sup1;&sup1;Truly, truly, I say to you, we speak of what we know, and bear witness to what we have seen, but you do not receive our testimony. &sup1;&sup2;If I have told you earthly things and you do not believe, how can you believe if I tell you heavenly things? &sup1;&sup3;No one has ascended into heaven except he who descended from heaven, the Son of Man. &sup1;⁴And as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, &sup1;⁵that whoever believes in him may have eternal life. </span>

<strong><span style="line-height: 1.6;">****** Result for searching Fruit Spirit ******** </span></strong>

<span style="line-height: 1.6;">Reference: Galatians 5:22 </span>

<span style="line-height: 1.6;">Text: But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness, </span>

<span style="line-height: 1.6;">Reference: Isaiah 32:15</span>

<span style="line-height: 1.6;">Text: until the Spirit is poured upon us from on high, and the wilderness becomes a fruitful field, and the fruitful field is deemed a forest. </span>

<strong><span style="line-height: 1.6;">****** Verse of the Day ******** </span></strong>

<span style="line-height: 1.6;">Reference :Psalm 23:1-3 </span>

<span style="line-height: 1.6;">Version :ESV </span>

<span style="line-height: 1.6;">The Lord is my shepherd; I shall not want. He makes me lie down in green pastures. He leads me beside still waters. He restores my soul. He leads me in paths of righteousness for his name&#39;s sake.</span></pre>
